import datetime

balance = 0

import hashlib
import getpass
import random



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def checkusernameexist(username, admin_username):
    return username == admin_username



def checkPassword(password, admin_password_hash):
    return hash_password(password) == admin_password_hash



def create_customer(Full_Name, NIC_NO, Phone_No):
    customer_id = str(random.randint(1000, 9999))
    print(f"{Full_Name}, your Customer_ID is: {customer_id}")

    with open("customer.txt", "a") as file:
        file.write(f"{customer_id},{Full_Name},{NIC_NO},{Phone_No}\n")
    



#===================================================== Function to login=======================================================
def login():
    
    admin_username = "Admin"
    admin_password = "Admin@123"  
    admin_password_hash = hash_password(admin_password)  
    
    
    with open("admin.txt", "w") as file:
        file.write(f"{admin_username},{admin_password_hash}\n")

    
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    
    if checkusernameexist(username, admin_username):
        if checkPassword(password, admin_password_hash):
            print(f"{username}, Welcome!")
        else:
            print("Invalid password")
            return False
    else:
        print("Invalid username")
        return False
    


login()  ##===========================login function colse==========================================================================




# #===================================== Admin menu=======================================

customer_Details = {}
balance={}
customer_id={}
while True:
    print("\n =====Admin Menu=====")
    print("1.Create Customer") 
    print("2.Customer Details")
    print("3.Exit")

    choice = int(input("Enter your choice option (1-4): "))
   
    if choice == 1:
        print("**************************")
        print("====Create Customer====")
        print("**************************")
        Full_Name = input("Enter Your Full Name:")
        NIC_NO = input("Enter Your NIC NO:")
        Phone_No = input("Enter Your Phone NO:")
        create_customer(Full_Name, NIC_NO, Phone_No)

    

    elif choice == 2:
        print("****************************")
        print("===All customer Details===")
        print("****************************")
        with open("customer.txt", "r") as file:
                for value in file:
                    test = value.split(",")
                    print(f"Customer ID: {test[0]}, "
                f"Customer Name: {test[1]}, "
                f"NIC: {test[2]}, "
                f"Phone Number: {test[3]}")

    elif choice == 3:
        print("*************")
        print("Exiting...")
        print("*************")
        break
    else:
        print("invalid choice")
##=============================== Admin colse=====================================================
    
# #####===================== Customer_Menu============================================
import random
last_deposit= 0
last_withdraw= 0
account_number=None



def Account_Create():
    return   str(random.randint(10000000,99999999))
account_number=Account_Create()




def show_balance(balance):
    print('************************')
    print(f"Your balance is Rs{balance:.2f}")
    print('************************')
    



def deposit():
    deposit= last_deposit 
    print('************************')
    amount = float(input("Enter an amount to be deposited: "))
    print('************************')

    if amount < 0:
        print('************************')
        print("That is not a valid amount")
        print('************************')
        return 0
    else:
        return amount




def withdraw(balance):
    withdraw =last_withdraw
    print('************************')
    amount = float(input("Enter amount to be withdrawn: "))
    print('************************')

    if amount > balance:
        print('************************')
        print("Insufficient funds")
        print('************************')
        return 0
    elif amount < 0:
        print('************************')
        print("Amount must be greater than 0")
        print('************************')
        return 0
    else:
        return amount




def Transaction_History(account_number, last_deposit, last_withdraw, balance):

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #global customer_id 
    with open("Transaction History.txt", "a") as file:
        file.write(
            f"Date | Time: {current_time} | " 
            f"Account: {account_number} | "
            f"Deposit: Rs.{last_deposit:.2f} | "
            f"Withdraw: Rs.{last_withdraw:.2f} | "
            f"Balance: Rs.{balance:.2f}\n"
            )



##======================================= read file=============================================================

def read_transaction_history():
    try:
        with open("Transaction History.txt", "r") as file:
            transaction_history = file.readlines()
            for transaction in transaction_history:
                print(transaction.strip())  
    except FileNotFoundError:
       print("Transaction History file not found.")

def money():
    customer_id = None
    history = []
    balance = 0
    is_running = True

    while is_running:
        print('************************')
        print(" ===Customer Menu===")
        print('************************')
        print("1. Account Create")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Balance")
        print("5. Transaction History")
        print("6. Exit")
        print('************************')
        choose = input("Enter your choice (1-6): ")

        if choose == '1':
            customer_id = Account_Create()
            print(f"{customer_id} Your Account has been created.")

        elif choose == '2':
            last_deposit= deposit()
            balance += last_deposit
            history.append(f"Deposited Rs {last_deposit:.2f}")

        elif choose == '3':
            last_withdraw = withdraw(balance)
            balance -= last_withdraw
            history.append(f"Withdrew Rs {last_withdraw:.2f}")

        elif choose == '4':
            show_balance(balance)

        elif choose == '5':
            print("Transaction History:")
            for i in history:
                print("-", i)
            

            Transaction_History(account_number, last_deposit, last_withdraw, balance)
            read_transaction_history()
            
        elif choose == '6':
            is_running = False
        else:
            print('************************')
            print("Not a valid choice")
            print('************************')

    print('************************')
    print("Thank you! Have a nice day")
    print('************************')



money()
