import re

title = "Password Strength Checker"
character = "-" * len(title)
print(character)
print(title)
print(character)

your_password = input("Enter password: ")
lower_case = r'[a-z]'
upper_case = r'[A-Z]'
special_characters = r'[!@#$%^&*()]'
numbers = r'\d'

if len(your_password) < 12:
    print("Password is too short. It should be at least 12 characters.")
elif not re.search(lower_case, your_password):
    print("Password should contain at least one lowercase letter.")
elif not re.search(upper_case, your_password):
    print("Password should contain at least one uppercase letter.")
elif not re.search(special_characters, your_password):
    print("Password should contain at least one special character.")
elif not re.search(numbers, your_password):
    print("Password should contain at least one number.")
else:
    print("Your password is strong :)")

