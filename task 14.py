print("Welcome to Swiss Bank")
name=input("Please Enter your name: ")
a=input("Enter your Account number: ")
b=input("Enter your pin: ")
print("Please choose options")
print("Enter 1, For Check Balance")
print("Enter 2, For Withdrawl Cash")
print("Enter 3, For Transfer money")
print("Enter 4, For Desposit")

x=int(input("Please Enter Your options: "))

match x:
    case 1:
        print("Your Account number: ", a)
        print(name ,"Your Balance is: 53456")
    case 2:
        print("Your Account number is: ", a)
        y=int(input("Enter Your Amount: "))
        r=53456-y
        print("Withdrawl Successfull")
        print("Your Balance is:" , r)
    case 3:
        print("Your Account number is: ", a)
        z=int(input("Enter your amount to transfer: "))
        p=int(input("Enter account number: "))
        print("Transfer successfull")
    case 4:
        print("Your account number: ", a)
        w=int(input("Enter your amount: "))
        e=53456+w
        print("Deposit Successfull")
        print("Your Balance is: ", e)
    case _:
        print("Please choose correct option")

