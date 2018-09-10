import unittest
from app.users import User
from app.orders import Order


class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.order = Order()

    def test_user_created_successfully(self):
        response = self.user.create_user("H", "Rigga", "hrigga21@gmail.com", "Password", "Password")
        self.assertEqual(response['msg'], 'User created successfully.')

    def test_signup_with_existing_email(self):
        self.user.create_user("H", "Rigga", "hrigga22@gmail.com", "Password", "Password")
        response = self.user.create_user("H", "Rigga", "hrigga22@gmail.com", "Password", "Password")
        self.assertEqual(response['msg'], 'Account with Email already exists. Please log in.')

    def test_signup_with_wrong_email_format(self):
        response = self.user.create_user("H", "Rigga", "hrigga@email", "Password", "Password")
        self.assertEqual(response['msg'], 'Please provide a valid email address')

    def test_signup_with_wrong_credentials(self):
        response1 = self.user.create_user("H", "Rigga", None, "Password", "Password")
        response2 = self.user.create_user(None, "Rigga", "hrigga22@gmail.com", "Password", "Password")
        response3 = self.user.create_user("H", None, "hrigga22@gmail.com", "Password", "Password")
        response4 = self.user.create_user("H", "Rigga", "hrigga22@gmail.com", None, "Password")
        response5 = self.user.create_user("H", "Rigga", "hrigga22@email.com", "Password80*", None)
        self.assertEqual(response1['msg'], 'Please input an email address')
        self.assertEqual(response2['msg'], 'Please input first name.')
        self.assertEqual(response3['msg'], 'Please input last name.')
        self.assertEqual(response4['msg'], 'Please input a password.')
        self.assertEqual(response5['msg'], 'Please confirm password.')

    def test_length_of_password(self):
        response = self.user.create_user("H", "Rigga", "hrigga23@email.com", "pass", "pass")
        self.assertEqual(response['msg'], 'Input a password that is at least 6 characters long.')

    def test_passwords_do_not_match(self):
        response = self.user.create_user("H", "Rigga", "hrigga23@gmail.com", "Password", "Passwort")
        self.assertEqual(response['msg'], 'Passwords do not match. Try again.')

    def test_failed_login(self):
        response = self.user.login_user("hrigga24@gmail.com", "Password")
        self.assertEqual(response['msg'], 'You have no account,please sign up')

    def test_successful_login(self):
        self.user.create_user("H", "Rigga", "hrigga25@gmail.com", "Password", "Password")
        response = self.user.login_user("hrigga25@gmail.com", "Password")
        self.assertEqual(response['msg'], 'Successfully logged in!')

    def test_login_with_wrong_credentials(self):
        response1 = self.user.login_user(None, "Password")
        response2 = self.user.login_user("hrigga25@gmail.com", None)
        self.assertEqual(response1['msg'], 'Please input an email address')
        self.assertEqual(response2['msg'], 'Please input a password.')

    def test_reset_password(self):
        self.user.create_user("H", "Rigga", "hrigga25@gmail.com", "Password", "Password")
        self.user.login_user("hrigga25@gmail.com", "Password")
        response = self.user.reset_password("hrigga25@email.com", "Passworda", "Passworda")
        self.assertEqual(response['message'], "Your password has been reset")
        response2 = self.user.reset_password("hrigga25@gmail.com", "Passworda", "Password")
        self.assertEqual(response2['msg'], "Passwords don't match")

    def test_failed_reset_password(self):
        response = self.user.reset_password("hrigga24@gmail.com", "Password", "Password")
        self.assertEqual(response['msg'], "You have no account, please sign up")

    def test_reset_password_wrong_credentials(self):
        response1 = self.user.reset_password(None, "Password", "Password")
        response2 = self.user.reset_password("hrigga25@gmail.com", None, "Password")
        response3 = self.user.reset_password("hrigga25@gmail.com", "Password", None)
        self.assertEqual(response1['msg'], 'Please input your email address')
        self.assertEqual(response2['msg'], 'Please input a new password.')
        self.assertEqual(response3['msg'], 'Please confirm your new password.')

    def test_new_order_placed(self):
        response = self.order.new_order("hrigga21@gmail.com", "what_order")
        self.assertEqual(response['message'], 'Order placed successfully.')

    def test_no_new_order_placed(self):
        response = self.order.new_order("hrigga22@gmail.com", None)
        self.assertEqual(response['msg'], 'Please place an order.')

    def test_delete_order(self):
        self.order.new_order("hrigga22@gmail.com", "what_order")
        response = self.order.delete_order(1)
        self.assertEqual(response['msg'], 'The order has been deleted successfully.')

    def test_failed_delete_order(self):
        self.order.new_order("hrigga22@gmail.com","what_order")
        response = self.order.delete_order(2)
        self.assertEqual(response['msg'], 'No such order exists.')

    def tearDown(self):
        del self.user
