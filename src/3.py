import random

def get_random_number(n):
    return random.randint(0, n)

def get_random_string(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join([alphabet[get_random_number(len(alphabet))] for _ in range(length)])
