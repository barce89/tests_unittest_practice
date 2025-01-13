import unittest
import os
from src.bank import BankAccount
from unittest.mock import patch
from src.exceptions import WithdrawalTimeRestrictionError
from datetime import datetime


class Test_BankAccount(unittest.TestCase):

    def setUp(self):#el metodo setUp es como un metodo para agregar o ocupar codigo que se repite en los demas
        self.account = BankAccount(balance=1000,log_file="transaction_log.txt")
    

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)


    def _count_lines(self,filename):
        with open(filename,"r")as f:
            return len(f.readlines())

    def test_deposit(self):
        # account = BankAccount(balance=1000)
        new_balance=self.account.deposit(300)
        self.assertEqual(new_balance,1300,'El balance no es igual')
        # assert new_balance==1300

    def test_withdraw(self):
        # account = BankAccount(balance=500)
        new_balance =self.account.withdraw(200)
        self.assertEqual(new_balance,800,'El balance no es igual')
        # assert new_balance == 800

    def test_get_balance(self):
        # account = BankAccount(balance=2000)
        # new_balance=account.deposit(500)
        # assert account.get_balance() == 2500
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(),1000)


    def test_transfer(self,amount = 500,target_account='4152 9439 9949'):
        self.account.transfer(amount,target_account)
        assert self.account.balance == 500

    def test_transaction_log(self):
        self.account.deposit(300)
        assert os.path.exists("transaction_log.txt")

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file)==1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file)==2


    @patch("src.bank.datetime")
    def test_withdraw_during_bussines_hours(self,mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.account.withdraw(100)


    @patch("src.bank.datetime")
    def test_withdraw_after_bussines_hours(self,mock_datetime):
        mock_datetime.now.return_value.hour = 17
        newbalance = self.account.withdraw(100)
        self.assertEqual(newbalance,900)
        

    # @patch("src.bank.datetime")
    # def test_weekend_days(self, mock_datetime):
    #     days_off = [5, 6]  # Sábado (5) y Domingo (6)

    #     for day in days_off:
    #         with self.subTest(day=day):  # Inicia una subprueba para cada día
    #             # Configura el mock para devolver el día y una hora fuera del horario laboral
    #             mock_datetime.now.return_value.weekday.return_value = day
    #             mock_datetime.now.return_value.hour = 7  # Configura una hora fuera del rango laboral (ej. 18:00)

    #             # Verifica que se genere la excepción esperada para días no laborables
    #             with self.assertRaises(WithdrawalTimeRestrictionError):
    #                 self.account.withdraw(100)  # Asume que este método genera la excepción


# este es otra manera de hacer la prueba de arriba :


    # @patch("src.bank.datetime")
    def test_weekend_days_2(self):
        test_cases = [
            {"ammount":100,"expected":1100},
            {"ammount":300,"expected":1300},
            {"ammount":4500,"expected":5500},
        ]
        for case in test_cases:
            with self.subTest(case=test_cases):
                self.account=BankAccount(balance=1000,log_file="")
                new_balance=self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])





#crear prueba unitaria para no retirar en domingo


# para poder hacer un reporte con con coverage es este comando desde terminal
# coverage run --source src -m unittest

# y despues el coverage report