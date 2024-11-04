from datetime import datetime

def get_days_from_today(date: str) -> int:
    today_date = datetime.today()
    provided_date = datetime.strptime(date, '%Y-%m-%d')

    return (today_date.date() - provided_date.date()).days

print(get_days_from_today('2024-10-03'))
print(get_days_from_today('2024-11-05'))
print(get_days_from_today('2025-10-03'))
print(get_days_from_today('2022-08-03'))
print(get_days_from_today('2024-11-03'))