import random

def get_random_code():
    numbers = "123456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(random.randint(10, 20)):
        code += random.choice(letters)
        if i % 3 == 0 and i != 0:
            code += "-"
    return code
