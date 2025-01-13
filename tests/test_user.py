from faker import Faker
import unittest,os
from src.user import User
from src.bank import BankAccount


class UserTests(unittest.TestCase):
    def setUp(self):
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(),email=self.faker.email())

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated,email=email_generated)
        self.assertEqual(user.name,name_generated)
        self.assertEqual(user.email,email_generated)

    def test_user_creation_multiple(self):
        
        for i in range(0,2):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100,max=200,step=50),
                log_file=self.faker.file_name(extension=".txt")
            )
            self.user.add_account(account=bank_account)
        
        expected =self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value,expected)

    def tearDown(self):
        for account in self.user.accounts:
            os.remove(account.log_file)
        



