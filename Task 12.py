#User input 
input=int(input("Please enter Bill amount:"))
if input>=5000:
    d=input*30/100
    print("You'll get 30% discount: " , d)
elif input>=2000 and input<=4999:
    d=input*20/100
    print("You'll get 20% discount", d)
elif input>=1000 and input<=1999:
    d=input*10/100
    print("You'll get 10% discount", d)
else:
    print("Add more to get more discount")
