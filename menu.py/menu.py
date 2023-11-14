# Accounts.py

class Account:
    def __init__(self, balance=0.0, interest_rate=0.0):
        self.balance = balance
        self.interest_rate = interest_rate

    def set_balance(self, balance):
        self.balance = balance

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate
# savings_account.py
from Accounts import Account

def create_savings_account(balance, interest_rate, user_input_interest):
    savings_account = Account(balance, interest_rate)
    
    # Calculating interest earned
    interest_earned = savings_account.balance * user_input_interest

    # Update account balance with earned interest
    savings_account.set_balance(savings_account.balance + interest_earned)

    return savings_account.balance, interest_earned
