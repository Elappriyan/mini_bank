

# balance = 0

# #======Admin user and password=================#####
# admin_username = "Admin"
# admin_password = "Admin@123"

# with open("admin.txt", "w") as file:
#     file.write(f"{admin_username},{admin_password}\n")
# import getpass

# def checkusernameexist(username):
#     return username == admin_username

# def checkPassword(password):
#     return password == admin_password

# def login():
#     username=input("Enter username: ")
#     password=getpass.getpass("Enter password: ")

#     if checkusernameexist(username):
#         if checkPassword(password):
#             print()
#             print(f"{username} Welcome")
#         else:
#             print("Invalid password")
#             return
#     else:
#         print("Invild username")
#         return
# login()



# #===================================== Admin menu=======================================

# customer_Details = {}
# balance={}

# while True:
#     print("\n =====Admin Menu=====")
#     print("1.Create Customer") 
#     print("2.Customer Details")
#     print("3.Exit")

#     choice = int(input("Enter your choice option (1-4): "))
   
#     if choice == 1:
#         print("**************************")
#         print("====Create Customer====")
#         print("**************************")
#         Full_Name = input("Enter Your Full Name:")
#         NIC_NO = input("Enter Your NIC NO:")
#         Phone_No = input("Enter Your Phone NO:")
        
    
        
#         import random
#         account_no=str(random.randint(10000000,99999999))
#         print(f"{Full_Name} Your Account No: {account_no}")

#         customer_Details={"Customer_Name":Full_Name, "NIC": NIC_NO , "Phone_Number":Phone_No , "Account_Number":account_no }

#         with open("customer.txt", "a") as file:
#             file.write(f"{account_no},{Full_Name},{NIC_NO},{Phone_No}\n")
           

#     elif choice == 2:
#         print("****************************")
#         print("===All customer Details===")
#         print("****************************")
#         with open("customer.txt", "r") as file:
#                 for value in file:
#                     test = value.split(",")
#                     print(f"Account No: {test[0]}, "
#                 f"Customer Name: {test[1]}, "
#                 f"NIC: {test[2]}, "
#                 f"Phone Number: {test[3]}")

#     elif choice == 3:
#         print("*************")
#         print("Exiting...")
#         print("*************")
#         break
#     else:
#         print("invalid choice")

    


    


# # #####===================== Customer_Menu=============================

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


# def money():
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
#           history.append(f"Deposited Rs ")
#         elif choose =='3':
#             balance -= withdraw(balance)
#             history.append(f"Withdraw Rs ")
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


# money()


