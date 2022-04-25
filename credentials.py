import random
import string


class Credentials:
    '''generating credentials for users'''
    credentials_list= []

    def __init__(self, app_name, user_name,password):
        self.app_name=app_name
        self.user_name=user_name
        self.password=password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

            