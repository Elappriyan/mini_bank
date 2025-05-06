customer_Details = {}
balance={}

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
        
    
        
        import random
        account_no=str(random.randint(10000000,99999999))
        print(f"{Full_Name} Your Account No: {account_no}")

        customer_Details={"Customer_Name":Full_Name, "NIC": NIC_NO , "Phone_Number":Phone_No , "Account_Number":account_no }

        with open("customer.txt", "a") as file:
            file.write(f"{account_no},{Full_Name},{NIC_NO},{Phone_No}\n")
           

    elif choice == 2:
        print("****************************")
        print("===All customer Details===")
        print("****************************")
        with open("customer.txt", "r") as file:
                for value in file:
                    test = value.split(",")
                    print(f"Account No: {test[0]}, "
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

    

