import random

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  
        self.total_balance = 0
        self.total_loan = 0

    def generate_account_number(self):
        return random.randint(100000, 999999)

    def create_account(self, name, email, address, ac_type):
        acct_number = self.generate_account_number()  

        
        balance = 0  
        transaction_history = []  

        self.accounts[acct_number] = {
            'name': name,
            'email': email,
            'address': address,
            'account_type': ac_type,
            'balance': balance,
            'transaction_history': transaction_history,
        }

        print(f"Account created successfully. Your account number is {acct_number}")
        return acct_number
