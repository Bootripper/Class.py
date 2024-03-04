print("Basic Calculator")
print("Press 1, for Addition")
print("Press 2, for Substraction")
print("Press 3, for Multiplication")
print("Press 4, for Division")

x=int(input("Enter Your no."))
    
a=int(input("Enter your Fisrt number"))
b=int(input("Enter your Second no."))

match x:
    case 1:
        c=a+b
        print("Addition", c)
    case 2:
        c=a-b
        print("Substraction",c)
    case 3:
        c=a*b
        print("Musltiplication", c)
    case 4:
        c=a/b
        print("Division", c)
    case _:
        print("please choose correct option")
