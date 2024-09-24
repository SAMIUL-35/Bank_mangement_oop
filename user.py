from login import *

class User(Login):
    def __init__(self, user_name, passd, bank):
        super().__init__(user_name, passd)
        
        
        if not Login.is_user_registered(user_name):
            users_login[self.user_name] = self.passd  
        else:
            print("User already registered.")
        
        self.balance = 0
        self.account = None  
        self.transaction_history = []
        self.loan_token = 0
        self.bank = bank 

    def create_account(self, name, email, address, ac_type):
        if self.account is not None:
            print("Account already exists! You can only create one account.")
        else:
            acct = self.bank.create_account(name, email, address, ac_type)
            self.account = acct  
            

    def deposit(self, amount):

    
        for acct_number, details in self.bank.accounts.items():
            if details['name'] == self.user_name:
           
                self.bank.accounts[acct_number]['balance'] += amount
                self.transaction_history.append(f"Deposited: {amount}")
                print(f"Deposited {amount} into account {acct_number}. New balance: {self.bank.accounts[acct_number]['balance']}")
            
           
                self.balance += amount
                self.bank.total_balance += amount
                return

        print("Account not found for this user.")

    def withdraw(self, amount):
        if Login.isBankrupt:
            print("Bank is bankrupt.")
        else: 
                      
             if amount > self.balance:
                print("Withdrawal amount exceeded.")
             else:
               for acct_number, details in self.bank.accounts.items():
                    if details['name'] == self.user_name:
                        self.balance -= amount
                        self.bank.accounts[acct_number]['balance'] -= amount
                        self.transaction_history.append(f"Withdrew: {amount}")
                        self.bank.total_balance -= amount
               print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        
        
        print(f"Available balance: {self.balance}")

    def check_transaction_history(self):
        
        
        print("Transaction history:")
        for transaction in self.transaction_history:
            print(transaction)

    
        
        
    def take_loan(self, amount):
        if not Login.loan:
            print("Loan system inactive.")
            return
            
    
        if self.loan_token >= 2:
            print("Loan limit reached.")
            return
    
        if self.bank.total_balance < amount:
            print("Bank is bankrupt.")
            return

   
        for acct_number, details in self.bank.accounts.items():
            if details['name'] == self.user_name:
            
                self.balance += amount
                self.bank.accounts[acct_number]['balance'] += amount 
                self.loan_token += 1
                self.transaction_history.append(f"Loan taken: {amount}")
                self.bank.total_loan += amount  
                print(f"Loan of {amount} approved. New balance: {self.balance}")
                return

        print("Account not found for this user.")


    def transfer(self, target_account, amount):
        if Login.isBankrupt:
            print("Bank is bankrupt.")
            return


        
        
        if target_account in self.bank.accounts:
            if amount > self.balance:
                print("Insufficient balance for transfer.")
            else:
                for acct_number, details in self.bank.accounts.items():
                    if details['name'] == self.user_name:
                        self.balance -= amount
                        self.bank.accounts[target_account]['balance'] += amount
                        self.bank.accounts[acct_number]['balance'] -= amount
                        self.transaction_history.append(f"Transferred: {amount} to {target_account}")
                print(f"Transferred {amount} to account {target_account}. New balance: {self.balance}")
        else:
            print("Target account does not exist.")
