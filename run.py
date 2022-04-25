#!/usr/bin/env python3.8
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


