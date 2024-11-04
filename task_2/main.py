import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    unique_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(unique_numbers)


if __name__ == "__main__":
    test_cases = [
        (1, 49, 6),
        (1, 36, 5),
        (10, 100, 10),
        (20, 50, 5),
        (1, 1000, 50),
        (5, 5, 1),
        (1000, 1000, 1),
        (1, 10, 11),
        (100, 50, 5),
        (0, 100, 5),
    ]

    for min_val, max_val, quantity in test_cases:
        lottery_numbers = get_numbers_ticket(min_val, max_val, quantity)
        print(f"Мін: {min_val}, Макс: {max_val}, Кількість: {quantity} => Числа: {lottery_numbers}")
