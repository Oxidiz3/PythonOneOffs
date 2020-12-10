import datetime

hours_mwf = 8
hours_ttr = 3
hourly_wage = 11


class WeekDay:
    def __init__(self, day_name, hrs_worked):
        self.name = day_name
        self.hrs_worked = hrs_worked


int_to_week_day = {
    1: WeekDay("Monday", hours_mwf),
    2: WeekDay("Tuesday", hours_ttr),
    3: WeekDay("Wednesday", hours_mwf),
    4: WeekDay("Thursday", hours_ttr),
    5: WeekDay("Friday", hours_mwf),
    6: WeekDay("Saturday", 0),
    7: WeekDay("Sunday", 0),
}


def day_number(day_in_range) -> int:
    days_since_today = datetime.datetime.now().day - day_in_range
    date_to_weekday = datetime.datetime.now().isoweekday() - days_since_today
    while date_to_weekday < 1:
        date_to_weekday += 7

    return date_to_weekday


def get_days_since_first():
    day_list = []
    days_since_first = datetime.datetime.now().day

    # for each day since the first day
    for day_in_range in reversed(range(1, days_since_first + 1)):
        day_list.append(int_to_week_day[(day_number(day_in_range))])

    return day_list


def money_earned_since_first(day_list):
    # TODO: finish this, then money earned all month
    total = 0

    for day in day_list:
        total += day.hrs_worked * hourly_wage

    return total


def __main__():
    day_list = get_days_since_first()
    month_money = money_earned_since_first(day_list)

    print(f"You have made ${month_money} so far this month")
    print(f"After Tithing and Tax you will have ${round(month_money*0.80, 2)}")


__main__()
