import datetime

days_list = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

def get_current_day():
    return days_list[datetime.datetime.now().weekday()]

def get_current_hour():
    return datetime.datetime.now().strftime("%H:00")