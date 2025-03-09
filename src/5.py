import random

def get_random_code():
    code = ''
    for i in range(8):
        code += str(random.randint(0, 9))
    return code