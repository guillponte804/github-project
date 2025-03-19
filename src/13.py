import random
from datetime import datetime

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def get_random_boolean():
    return random.choice([True, False])

def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for i in range(length))

def get_random_date():
    return datetime.strptime('%d/%m/%Y', '%d/%m/%Y').date()

def get_random_datetime():
    return datetime.strptime('%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M:%S')

def main():
    print(get_random_number(1, 10))
    print(get_random_boolean())
    print(get_random_string(10))
    print(get_random_date())
    print(get_random_datetime())

if __name__ == '__main__':
    main()