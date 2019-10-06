#!/usr/bin/env python3

import re
from getpass import getpass


def validate_email(email):
    return re.match(r'[^@]+@[^@]+\.[^@]+', email)


def validate_password(password):
    return re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', password)


def main():
    while True:
        try:
            if validate_email(input('Enter your email address: ')):
                break
            else:
                raise Exception('Error: invalid email format')
        except Exception as e:
            print(e)

    print(
        '''
Password must contain:
  1 lowercase letter
  1 uppercase letter
  1 number
  1 special character
'''
    )

    while True:
        try:
            if validate_password(getpass('Choose a password: ')):
                break
            else:
                raise Exception('Error: invalid password format')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
