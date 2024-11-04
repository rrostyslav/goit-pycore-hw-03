import re

def normalize_phone(phone_number: str) -> str:
    phone_number = re.sub(r'\D', '', phone_number)
    match = re.search(r'(?P<start>(\+?\d{0,3}))?\s*(\d{10})', phone_number)

    if match:
        start = match.group('start')
        if not start or start != "+38":
            phone_number = '+38' + match.group(3)
        else:
            phone_number = '+' + start + match.group(3)

    return phone_number

if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
