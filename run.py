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
        