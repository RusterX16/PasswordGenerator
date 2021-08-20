# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
import random


# power 0 : Uppercase and lowercase letters
# power 1 : Uppercase and lowercase Letters and numbers
# power 2 : Uppercase and lowercase letters, numbers and special characters
def password_generator(length, power):
    password = ""
    if power == 0:
        password = ''.join(random.choices(string.ascii_letters, k = length))
    elif power == 1:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k = length))
    elif power == 2:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = length))
    else:
        print("Invalid power")
    return password


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(password_generator(8, 0))
    print(password_generator(12, 1))
    print(password_generator(16, 2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
