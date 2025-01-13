import unittest

from test_bank import Test_BankAccount

def bank_account_suite():
    suite=unittest.TestSuite()
    suite.addTest(Test_BankAccount('test_deposit'))
    suite.addTest(Test_BankAccount('test_withdraw'))
    return suite

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())