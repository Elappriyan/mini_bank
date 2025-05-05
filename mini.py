# name=input("Enter your Name :")
# acc_no= input("create Account number: ")
# password=input("8-digal,@,#,$ use full :")



# file=open("user.txt",'w')
# file.write(f"Enter your name:{name}\n")
# file.write(f"Enter your acc_no:{acc_no}\n")
# file.write(f"Enter your password:{password}\n")
# file.close()



balance = 0

##===================
admin_username = "Admin"
admin_password = "Admin@123"



import getpass

def checkusernameexist(username):
    return username == admin_username

def checkPassword(password):
    return password == admin_password

def login():
    username=input("Enter username: ")
    password=getpass.getpass("Enter password: ")

    if checkusernameexist(username):
        if checkPassword(password):
            print()
            print(f"{username} Welcome")
        else:
            print("Invalid password")
    else:
        print("Invild username")
login()



#===================================== Admin menu=======================================

customer_Details = {}

while True:
    print("\n =====Admin Menu=====")
    print("1.Create Customer") 
    print("2.Customer Details")
    print("3.Exit")

    choice = int(input("Enter your choice option (1-4): "))
    
    if choice == 1:
        Full_Name = input("Enter Your Full Name:")
        NIC_NO = input("Enter Your NIC NO:")
        Phone_No = input("Enter Your Phone NO:")

        import random
        account_no=random.randint(10000000,99999999)
        print(f"{Full_Name} Your Account No: {account_no}")

        customer_Details={"Customer_Name":Full_Name, "NIC": NIC_NO , "Phone_Number":Phone_No , "Account_Number":account_no }

     
    elif choice == 2:
        print("===All customer Details===")


        for customer in  customer_Details:
            print(f"Account No:{customer['account_no']},"
                  f"Customer_Name:{customer['Full_Name']},"
                  f"NIC:{customer['NIC_NO']},"
                  f"Phone_Number:{customer['Phone_No']}")
        
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("invalid choice")

    



    


# #####===================== Customer_Menu=============================

# def show_balance(balance):
#     print('************************')
#     print(f"Your balance is Rs{balance:.2f}")
#     print('************************')




# def deposit():
 
#     print('************************')
#     amount =float(input("Enter an amount to be deposited: "))
#     print('************************')

#     if amount < 0:
#         print('************************')
#         print("That is not a valid amount")
#         print('************************')
#         return 0
#     else:
#            return amount




# def  withdraw(balance):
   
#     print('************************')
#     amount = float(input("Enter amount to be withdraw: "))
#     print('************************')

#     if amount > balance:
#         print('************************')
#         print(" insufficient funds")
#         print('************************')
#         return 0
#     elif amount < 0:
#         print('************************')
#         print("Amonut must be greater than 0")
#         print('************************')
#         return 0
#     else:
#         return amount


# def main():
#     history=[]
#     balance = 0
#     is_running = True
#     amount={}
#     while is_running :
#         print('************************')
#         print(" ===Customer Menu===")
#         print('************************')
#         print("1.Show Balance")
#         print("2.Deposit")
#         print("3.Withdraw")
#         print("4.Transaction History")
#         print("5.Exit")
#         print('************************')
#         choose = input("Enter your choose(1-5):")


#         if choose =='1':
#             show_balance(balance)
#         elif choose =='2':
#           balance += deposit()
#           history.append(f"Deposited Rs {amount:.2f}")
#         elif choose =='3':
#             balance -= withdraw(balance)
#             history.append(f"Withdraw Rs {amount:.2f}")
#         elif choose =='4':
#              for i in history:
#                  print("-",i)
    
#         elif choose =='5':
#             is_running =False
#         else: 
#             print('************************')
#             print(" Not a valid choice") 
#             print('************************')

#     print('************************')
#     print("Thank you! have a nice day")
#     print('************************')


# if __name__=='__main__':
#   main()


