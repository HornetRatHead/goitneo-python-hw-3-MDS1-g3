import datetime
from collections import defaultdict

users = [
    {'name': 'Bill Gates', 'birthday': datetime.date(1955, 10, 28)},
    {'name': 'Kim Kardashian', 'birthday': datetime.date(1980, 10, 21)},
    {'name': 'Jill Valentine', 'birthday': datetime.date(1974, 10, 24)},
    {'name': 'Jan Koum', 'birthday': datetime.date(1976, 10, 27)},
    {'name': 'Steve Jobs', 'birthday': datetime.date(1955, 2, 24)},
    {'name': 'Hala Penio', 'birthday': datetime.date(1976, 2, 29)},
]

#Перевіряемо чи є рік високосним 
current_year = datetime.datetime.now().year
def leap_year (current_year):
    if current_year % 4 == 0:
        if current_year % 100 != 0 or current_year % 400 == 0:
            return True
    return False


def get_birthdays_per_week(users):

    if not users:
        return[]


    today = datetime.date.today()
    birthdays = defaultdict(list)
    work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for user in users:
        name = user["name"]
        birthday = user['birthday']

    #Перевіряемо чи не народилася людина 02.29 та робимо "spike"
        if birthday.month == 2 and birthday.day == 29 and not leap_year(current_year):
            current_birthday = datetime.date(current_year, 3, 1)
        else:
            current_birthday = birthday.replace(year=today.year)
            print(current_birthday)
    
        if current_birthday < today:
         current_birthday = current_birthday.replace(year=today.year + 1)
    
        delta_days = (current_birthday - today).days
        if 0 <= delta_days < 7:
            weekday = current_birthday.weekday()

            if weekday >= 5:
                weekday = 0
        
            birthdays[work_days[weekday]].append(name)

    current_week_celebration = {}   
    for day, names in birthdays.items():
        current_week_celebration[day] = ', '.join(names)

    return current_week_celebration


if __name__ == "__main__":
    print(get_birthdays_per_week(users))