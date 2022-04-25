#!/usr/bin/env python3.8
from hashlib import new
from credentials import Credentials
from user import User
import string
from random import *

def create_user(username,password):
    '''funtion to create new user'''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''saving the user'''
    user.save_user()

def delete_user(user):
    '''deleting the user'''
    user.delete_user()

def display_user(cls):
    '''displaying user method'''
    return User.display_user()          


def create_credentials(app_name,username,password):
    '''creating new credentials function'''
    new_credentials = Credentials(app_name,username,password)
    return new_credentials

def save_credentials(credentials):
    '''saving credentials'''
    credentials.save_credentials()   

def delete_credentials(credentials):
    '''deleting credentials'''
    credentials.delete_credentials()      

def display_credentials():
    '''returning method for creentials'''
    return Credentials.display_credentials()

def find_credential():
    '''finding method for credentials'''   
    return Credentials.find_credentials()

def main():

    print("Hello Welcome to your passwordlocker. What is your name?")

    print('Create account:')
    print('-'*10)
    print('Username...')
    user_name = input()
    print('Password...')
    password = input()

    print(f'Your account {user_name} has been successfully created!!')

    print('Login:')
    print('Username...')
    user_name = input()
    print('Password...')
    password = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        
        print("Use these short codes : cc - create a new account, dc - display credetials fc -find a credentials, ex -exit the credentials list ")
        short_code = input()

        if short_code == 'cc':
            print("Create Credentials account")
            print("-"*10)

            print ("user name ....")
            user_name = input()

            print("App Name ...")
            app_name = input()
            print("Password ...")
            password = input()

            save_credentials(create_credentials(user_name,app_name,password))
            print ('\n')
            print(f"New credentials {user_name} {app_name} created")

            
            print ('\n')

        elif short_code == 'dc':
            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credentials in display_credentials():
                    print(f"{credentials.user_name} {credentials.app_name} .....{credentials.password}")

                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')
        elif short_code == 'fc':

            print("Enter the account name you want to search for")

            search_credentials = input()
            if existing_credentials(search_credentials):
                search_credentials = find_credential(search_credentials)
                print(f"{search_credentials.app_name} {search_credentials.user_name}")
                print('-' * 20)

                print(f"Phone number.......{search_credentials.password}")
            else:
                print("That Account does not exist")

if __name__ == '__main__':
    main()