from datetime import datetime
from src.exceptions import WithdrawalTimeRestrictionError


class BankAccount():
    def __init__(self,balance = 0,log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creadas')



    def _log_transaction(self,message):
        if self.log_file:
            with open(self.log_file,"a")as f:
                f.write(f'{message}\n')



    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount} .New balance: {self.balance}")
        return self.balance
    
    
    # def withdraw(self,amount):
    #     now=datetime.now()
    #     if now.hour < 8 or now.hour >17:
    #         raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8 am to 5 pm")

    #     if now.weekday() == 6:
    #         raise WithdrawalTimeRestrictionError("Withdrawals are not allowed on Sundays.")

    #     if amount>0:
    #         self.balance -= amount
    #         self._log_transaction(f"Withdraw {amount} .New balance: {self.balance}")
    #     return self.balance
    
    def withdraw(self, amount):
        # now = datetime.now()
        # # No se permite retirar fuera de horario
        # if now.hour < 8 or now.hour > 17:
        #     raise WithdrawalTimeRestrictionError("Retiros fuera de horario no están permitidos.")
        # # No se permite retirar los domingos
        # if now.weekday() == 6:  # 6 es domingo
        #     raise WithdrawalTimeRestrictionError("No se permite retirar los domingos.")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente.")
        self.balance -= amount
        return self.balance


    
    def get_balance(self):
        self._log_transaction(f"Checked balance .New balance: {self.balance}")
        return self.balance
    
    def transfer(self,amount,target_account):
        if self.balance<amount:
            
            raise ValueError('Insufficient funds.')
        self.withdraw(amount)
        return f'tenemos de balance {self.balance}, fue transferido ${amount} a la cuenta {target_account}'


