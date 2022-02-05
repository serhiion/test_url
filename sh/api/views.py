from datetime import datetime, timedelta
import random

from flask import abort, request, redirect, jsonify

from app import app, db
from api.errors import NoResourceFound, InvalidUsage, ApiError, NotAllowed
from api.helpers import validate_url
from api.models import Link, link_schema


URL_ALPHABET = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789'
URL_SIZE = 7


def get_short_url() -> str:
    while True:
        short = ''.join(random.choices(URL_ALPHABET, k=URL_SIZE))
        if Link.query.filter_by(short=short).first() is None:
            return short


@app.errorhandler(ApiError)
def handle_error(error: ApiError) -> str:
    return jsonify(error.to_dict())


@app.route("/<string:short>")
def redirect_to(short: str) -> str:
    link = Link.get_from_short(short)
    if link is None:
        abort(404)

    if link.is_one_off:
        link.deleted_at = datetime.utcnow()
        db.session.commit()
    return redirect(link.src, 301)


@app.route("/links/<string:short>", methods=["GET", "POST", "PUT", "DELETE"])
def get_link(short: str) -> str:
    if short == "" or request.method in ["POST", "PUT", "DELETE"]:
        raise NotAllowed("Method not allowed")

    link = Link.get_from_short(short)
    if link is None:
        raise NoResourceFound("No link found")
    return link_schema.dump(link)


@app.route("/links", strict_slashes=False, methods=["POST"])
def create_link():
    r = request.json
    if r is None or not validate_url(r.get("src")):
        raise InvalidUsage("Wrong URL format", 401)

    rand_short = get_short_url()
    try:
        link = Link(
            src=r["src"],
            short=rand_short,
            deleted_at=datetime.utcnow() +
            timedelta(minutes=10) if bool(r.get("expiring")) else None,
            is_one_off=bool(r.get("is_one_off")))
    except TypeError:
        raise InvalidUsage("Wrong JSON data format", 401)

    db.session.add(link)
    db.session.commit()
    return link_schema.dump(link), 201
