To start: docker-compose up --build
http://0.0.0.0:5001/links/ (POST)
{
    "src" : "https://ua.jooble.org/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-junior-python/%D0%9A%D0%B8%D0%B5%D0%B2" 
}

{
    "deleted_at": null,
    "expiring": false,
    "is_one_off": false,
    "short": "3G2Hc73",
    "src": "https://ua.jooble.org/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-junior-python/%D0%9A%D0%B8%D0%B5%D0%B2"
}

src - Початкова лінка
is_one_off - Флажок для однозвязності
expiring - Можливість удалити через певний час (10 хв)
short - Змінена силка
deleted_at - Коли силка буде видалена, якщо постійна - null

http://0.0.0.0:5001/3G2Hc73/ - NEW LINK
