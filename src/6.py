import random
def get_random_code():
    codes = {
        "0": ["0", "1", "2"],
        "1": ["3", "4", "5"],
        "2": ["6", "7", "8"],
        "3": ["9", "A", "B"],
        "4": ["C", "D", "E"],
        "5": ["F", "G", "H"],
        "6": ["I", "J", "K"],
        "7": ["L", "M", "N"],
        "8": ["O", "P", "Q"],
        "9": ["R", "S", "T"],
        "A": ["U", "V", "W"],
        "B": ["X", "Y", "Z"],
    }
    code = ""
    for i in range(8):
        code += random.choice(codes[str(i)])
    return code