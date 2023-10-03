import random
import string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
long_words = ["apple", "guava", "python", "date", "codsoft"]  

password_length = int(input("Enter the desired length of the password: "))
password_complexity = int(input("Enter the desired complexity of the password (1-3): "))

complexity_requirements = {
    1: [lowercase_letters, uppercase_letters, digits],
    2: [lowercase_letters, uppercase_letters, digits, symbols],
    3: [lowercase_letters, uppercase_letters, digits, symbols, long_words]
}

used_characters = set()
password = ""
for i in range(password_length):
    password_requirement = random.choice(complexity_requirements[password_complexity])

    if password_requirement == lowercase_letters:
        character = random.choice(lowercase_letters)
    elif password_requirement == uppercase_letters:
        character = random.choice(uppercase_letters)
    elif password_requirement == digits:
        character = random.choice(digits)
    elif password_requirement == symbols:
        character = random.choice(symbols)
    elif password_requirement == long_words:
        character = random.choice(long_words)

    if character not in used_characters:
        password += character
        used_characters.add(character)

print("Generated password:", password)
