from datetime import date


def calculate_birthday_countdown(birthday):
    """
    Возвращает количество дней до дня рождения
    Если день рождения сегодня возвращает 0
    """
    today = date.today()
    bd_this_year = get_birthday_for_year(birthday, today.year)

    if bd_this_year < today:
        next_birthday = get_birthday_for_year(bd_this_year, today.year+1)
    else:
        next_birthday = bd_this_year

    birthday_countdown = (next_birthday - today).days
    return birthday_countdown

def get_birthday_for_year(birthday, year):
    """
    Получает дату дня рождения на конкретный год

    Ошибка ValueError возможно только в високосном году
    и когда ДР выпадает на 29 февраля
    В этом случае дата ДР приравнивается к 1 марта
    """

    try:
        calculated_date = birthday.replace(year=year)
    except ValueError:
        calculated_date = date(year=year, month=3, day=1)
    return calculated_date
