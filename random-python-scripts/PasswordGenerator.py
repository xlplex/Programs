import random
import string
import os

if not os.path.exists('password.txt'):
    open('password.txt', 'w+').close()

def generate_password(length, use_digits=True, use_letters=True, use_special_chars=True):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_letters:
        characters += string.ascii_letters
    if use_special_chars:
        characters += string.punctuation

    if not (use_digits or use_letters or use_special_chars):
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    length = int(input("Enter the length of the password: "))
    use_digits = input("Use digits (0123456789)? (y/n): ").lower() == 'y'
    use_letters = input("Use letters (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)? (y/n): ").lower() == 'y'
    use_special_chars = input("Use special characters (!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_letters, use_special_chars)
    print(f"Generated Password: {password}")
    file = open('password.txt', 'a')
    file.write(password)
    file.close


if __name__ == "__main__":
    main()
