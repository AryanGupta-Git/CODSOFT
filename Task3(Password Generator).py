import random
import string

pswd_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
pswd_length = int(input("Enter the desired length of the password: "))

password = ""
for i in range(pswd_length):
    password += random.choice(pswd_char)
print("Generated password:", password)

password_complexity = int(input("Enter the desired complexity of the password (1-3): "))
complexity_requirements = {
    1: ["lower", "upper", "numbers"],
    2: ["lower", "upper", "numbers", "symbols"],
    3: ["lower", "upper", "numbers", "symbols", "long words (>5 characters)"]
}
password = ""
for i in range(pswd_length):
    pswd_requirement = random.choice(complexity_requirements[password_complexity])

    if pswd_requirement == "lower":
        password += random.choice(pswd_char.lower())
    elif pswd_requirement == "upper":
        password += random.choice(pswd_char.upper())
    elif pswd_requirement == "numbers":
        password += random.choice(string.digits)
    elif pswd_requirement == "symbols":
        password += random.choice(string.punctuation)
    elif pswd_requirement == "long words":
        password += random.choice(pswd_char.split())

print("Generated password:", password)