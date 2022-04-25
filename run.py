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
    Credentials.save_credentials()    

def delete_credentials(credentials):
    '''deleting credentials'''
    Credentials.delete_credentials()      

def display_credentials(cls):
    '''returning method for creentials'''
    return Credentials.delete_credentials()

def find_credentials(credentials):
    '''finding method for credentials'''   
    return Credentials.find_credentials()

def main():
     print("Hello Welcome to your passwordlocker. What is your name?")
     user_name = input()

     print(f"Hello {user_name}. what would you like to Login(LOGIN)?")
     print('\n')

     while True:
        
        print("Use these short codes : cc - create a new account, dc - display credetials fc -find a credentials, ex -exit the credentials list ")

if short_code == 'cc':
            print("LOGIN")
            print("-"*10)

            print ("user name ....")
            user_name = input()

            print("password ...")
            password = input()

        save_contacts(create_user(user_name,password)) # create and save new ser.
            print ('\n')
            print(f"New User {user_name} {password} created")
            print ('\n')