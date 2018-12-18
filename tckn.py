import random
import string


def generate() -> str:
    digits = range(10)
    first_9_digits = random.choices(digits, k=9)
    digit_10 = (sum(first_9_digits[::2]) - sum(first_9_digits[1::2])) % 10
    first_10_digits = first_9_digits + [digit_10]
    digit_11 = sum(first_10_digits) % 10
    all_digits = first_10_digits + [digit_11]
    return ''.join(str(digit) for digit in all_digits)


def validate(number: str) -> bool:
    if len(number) != 11:
        return False
    if not all(d in string.digits for d in number):
        return False
    digits = [int(d) for d in number]
    if digits[9] != (sum(digits[:9:2]) - sum(digits[1:9:2])) % 10:
        return False
    if digits[10] != sum(digits[:10]) % 10:
        return False
    return True