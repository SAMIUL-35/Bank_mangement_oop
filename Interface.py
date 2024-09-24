from user import User
from admin import Admin
from bank import Bank
from login import Login  

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
