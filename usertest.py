import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user=User('Mbogani','000')

    def tearDown(self):
        User.user_list=[] 

        '''actual test'''

    def test_init(self):
        self.assertEqual(self.new_user.username,'Mbogani')  
        self.assertEqual(self.new_user.password,'000')  

    def test_save_user(self):
        '''test to see if user has been added'''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user=User('username','000')
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)    


    def test_display_all_user(self):
        '''method that return a list of all users'''

        self.assertEqual(User.display_user(),User.user_list)    
        


if __name__ == '__main__':
    unittest.main()
