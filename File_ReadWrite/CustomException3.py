class PasswordLength(Exception):
    pass
try:
    password=input("Enter password ")
    if len(password)<8:
        raise PasswordLength
except PasswordLength:
    print("Password Must be greater then 8 letters ")