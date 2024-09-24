from login import *

class Admin(Login):
    def __init__(self, user_name, passd, bank):
        super().__init__(user_name, passd)
        self.bank = bank
        
        
        if not Login.is_user_registered(user_name):
           users_login[user_name] = passd  

    def create_account(self, name, email, address, ac_type):
        self.bank.create_account(name, email, address, ac_type)

    def delete_account(self, acct_number):
        if acct_number in self.bank.accounts:
            balance = self.bank.accounts[acct_number]["balance"]
            del self.bank.accounts[acct_number]
            self.bank.total_balance -= balance
            print(f"Account {acct_number} deleted successfully.")
        else:
            print("Account does not exist.")

    def view_all_accounts(self):
        print("All accounts:")
        for account_num, details in self.bank.accounts.items():
            print(f"Account Number: {account_num}, Name: {details['name']}, Balance: {details['balance']}")

    def check_total_balance(self):
        print(f"Total bank balance: {self.bank.total_balance}")

    def check_total_loan(self):
        print(f"Total Loan balance: {self.bank.total_loan}")

    def toggle_loan_feature(self):
        Login.loan = not Login.loan
        status = "enabled" if Login.loan else "disabled"
        print(f"Loan feature has been {status}.")
    def Banrupt(self):
        Login.isBankrupt = not Login.isBankrupt
        status = "enabled" if Login.isBankrupt else "disabled"
        print(f"Bankrupt feature has been {status}.")