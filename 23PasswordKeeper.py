'''This script keeps your password and reveals it if you correctly write the user name. '''

user_name = 'Joseph'
passwrd = 'W@12"'

first_name = input('What\'s your first name? ')
first_name = first_name.capitalize()
if first_name == user_name:
    print('Hello Joseph! The password is: ', passwrd)
else:
    print('Hello, {}! See you later.'.format(first_name))