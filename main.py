import random
users_login = {}  

class Login:
    loan = True
    isBankrupt=False
    
    def __init__(self, user_name, passd):
        self.user_name = user_name
        self.passd = passd

    @classmethod
    def is_user_registered(cls, name):
        return name in users_login
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


bank = Bank("SHADIN BANK")
print(f"\t**************** Welcome to {bank.name} *************************\t")


while True:
    print("Choose your role:\n1. User\n2. Admin\n3. Exit")
    role = input("Enter your option: ")

    if role == "1": 
        name = input("Enter your name: ")
        password = input("Enter your password:\t ")

        if Login.is_user_registered(name):  
            user = User(name, password, bank)  
            print(f"Welcome {name}!\t")

            while True:
                print("\nUser Menu:")
                print("1. Create Account")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Check Balance")
                print("5. Transaction History")
                print("6. Take Loan")
                print("7. Transfer Money")
                print("8. Exit\t")
                action = input("Choose an action: ")

                if action == "1":  
                    email = input("Enter your email: ")
                    address = input("Enter your address: ")
                    ac_type = input("Enter account type (Savings/Current): ")
                    user.create_account(name, email, address, ac_type)

                elif action == "2":  
                    amount = int(input("Enter amount to deposit: "))
                    user.deposit(amount)

                elif action == "3":  
                    amount = int(input("Enter amount to withdraw: "))
                    user.withdraw(amount)

                elif action == "4":  
                    user.check_balance()

                elif action == "5":  
                    user.check_transaction_history()

                elif action == "6":  
                    amount = int(input("Enter loan amount: "))
                    user.take_loan(amount)

                elif action == "7":  
                    print("one user have only one account.so for transfer ,create another user and account")
                    target_account = int(input("Enter target account number: "))
                    amount = int(input("Enter amount to transfer: "))
                    user.transfer(target_account, amount)


                elif action == "8":  
                    break

                else:
                    print("Invalid option. Try again.")
        else:
            print("User not registered. Pls register first.")
            name = input("Enter user Registration  name: ")
            password = input("Enter user Registration password: ")
            user = User(name, password, bank) 
            print("login against Register user") 
            
            

    elif role == "2":  
        name = input("Enter admin name: ")
        password = input("Enter admin password: ")

        if Login.is_user_registered(name):  
            admin = Admin(name, password, bank)  
            print("Welcome Admin!\t")

            while True:
                print("\nAdmin Menu:")
                print("1. Create User Account")
                print("2. Delete User Account")
                print("3. View All Accounts")
                print("4. Check Total Bank Balance")
                print("5. Check Total Loan Amount")
                print("6. Toggle loan on and off ")
                print("7. bankrupt Actvated ")
                print("8. Exit\t")
                action = input("Choose an action: ")

                if action == "1":  
                    name = input("Enter account holder's name: ")
                    email = input("Enter account holder's email: ")
                    address = input("Enter account holder's address: ")
                    ac_type = input("Enter account type (Savings/Current): ")
                    admin.create_account(name, email, address, ac_type)

                elif action == "2":  
                    acct_number = int(input("Enter account number to delete: "))
                    admin.delete_account(acct_number)

                elif action == "3":  
                    admin.view_all_accounts()

                elif action == "4":  
                    admin.check_total_balance()

                elif action == "5":  
                    admin.check_total_loan()

                elif action == "6": 
                   admin.toggle_loan_feature() 
                elif action == "7": 
                   admin.Banrupt() 
                    
                elif action == "8":  
                    break

                else:
                    print("Invalid option. Try again.\t")
        else:
            print("Admin not registered. Please Register first.\t")
            name = input("Enter admin Registration  name: ")
            password = input("Enter admin Registration password: ")
            admin = Admin(name, password, bank)  
            print("login against Register admin") 
            
            
    elif role == "3":  
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid role. Please choose either '1' for User, '2' for Admin, or '3' to Exit.")
