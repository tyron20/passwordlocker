class User:
    '''creation of new user...'''

    user_list=[]

    def __init__(self, username, password):
        self.username=username
        self.password=password    

    def save_user(self):
        '''saving user function'''
        User.user_list.append(self)  

    def delete_user(self):
        '''delete user function'''
        User.user_list.remove(self)    
    
    @classmethod
    def display_user(cls):
        '''the method that shows user_list'''
        return cls.user_list

    def login_user(username,password):
        '''function that checks whether a user exists'''  
        check_user=User.verify_user(username,password)
        return check_user  

         

