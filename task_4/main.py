from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= today + timedelta(days=6):
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "2000.11.03"},
        {"name": "Jane Smith", "birthday": "2000.11.04"},
        {"name": "Alice Johnson", "birthday": "2000.11.05"},
        {"name": "Bob Brown", "birthday": "1990.11.06"},
        {"name": "Charlie Davis", "birthday": "1990.11.09"},
        {"name": "Eve Black", "birthday": "2004.11.10"},
        {"name": "Alice Smith", "birthday": "1995.12.24"},
        {"name": "Frank White", "birthday": "2004.11.07"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)

    print("Список привітань на цьому тижні:", upcoming_birthdays)
