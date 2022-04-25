
import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials('Instagram','Mbogani','000')

    def tearDown(self):
        Credentials.credentials_list=[]

    def test_init(self):
        self.assertEqual(self.new_credentials.app_name,'Instagram')
        self.assertEqual(self.new_credentials.user_name,'Mbogani') 
        self.assertEqual(self.new_credentials.password,'000')  

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    # def test_save_multiple_credentials(self):
    #     self.new_credentials.save_credentials()
    #     test_credential= Credentials('Twitter', 'username', '0000')
    #     test_credential.save_credentials()
    #     self.assertEqual(len(Credentials.credentials_list),2) 
    #     def test_delete_contact(self):
    def test_delete_credentials(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_credentials.save_credentials()
        test_credentials= Credentials('Instagram','Mbogani','000') # new credentials
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()

    def test_display_all_credentials(self):
        '''method that returns all saved credentials'''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)   



if __name__=='__main__':
    unittest.main()        
