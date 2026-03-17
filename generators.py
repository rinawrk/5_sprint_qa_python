import random

def generate_name():
    return f"Rina{random.randint(1, 9)}"

def generate_email():
    return f"irina_mikheeva_41_{random.randint(100, 999)}@yandex.ru"

def generate_valid_password():
    return f"P@ss{random.randint(10, 99)}"

def generate_invalid_password():
    return f"P@ss{random.randint(1, 9)}"
