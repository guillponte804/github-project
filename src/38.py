import os
os.system('clear')  # Clear screen to make it easier to read

def main():
    user_input = input("Enter your name: ")
    
    if not user_input.isalpha():
        print(f"Invalid input! Please enter a valid alphabetical character.")
        return
    
    else:
        print(f"Hello, {user_input}. Welcome!")

if __name__ == "__main__":
    main()
