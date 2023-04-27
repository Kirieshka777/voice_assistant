import datetime as dt
UTC = {
    'Ростов на дону': 3,
    'Москва':3,
    'Саратов':4,
    'Петропавловск Камчатский':12
}
def kgj():
    city = input('')
    utc_time = dt.datetime.utcnow()
    try:
        time = dt.timedelta(hours=UTC[city])
        city_time = utc_time + time
        print(city_time)
    except KeyError:
        print('Я не знаю')
kgj()