import random

print("******* Welcome to the password generator ********")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W',
           'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['#', '*', '@', '$', '!', '^', '(', ')']

user_letter = int(input("How many letters you need?\n"))
user_num = int(input("How many numbers you need?\n"))
user_special_chars = int(input("How many special characters you need?\n"))

password = []

for char in range(1, user_letter + 1):
    password += random.choice(letters)

for char in range(1, user_num + 1):
    password += random.choice(numbers)

for char in range(1, user_special_chars + 1):
    password += random.choice(special_chars)

random.shuffle(password)

password_final = ''
for char in password:
    password_final += char

print(f"Your password is {password_final}")
