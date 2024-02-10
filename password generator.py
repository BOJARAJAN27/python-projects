import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{};:,./?"

length = int(input("Enter the password length: "))

use_letters = input("Use letters? (yes/no): ") == "yes"
use_numbers = input("Use numbers? (yes/no): ") == "yes"
use_symbols = input("Use symbols? (yes/no): ") == "yes"

if not (use_letters or use_numbers or use_symbols):
	print("You must use at least one character type.")
	exit()

password = ""

char_types = []
if use_letters:
	char_types.append(letters)
if use_numbers:
	char_types.append(numbers)
if use_symbols:
	char_types.append(symbols)

for i in range(length):
	char_type = random.choice(char_types)
	char = random.choice(char_type)
	password += char

print("Your password is:", password)
