#User input 
input=int(input("Please enter Bill amount:"))
if input>=5000:
    print("You'll get 30% discount")
elif input>=2000 and input<=4999:
    print("You'll get 20% discount")
elif input>=1000 and input<=1999:
    print("You'll get 10% discount")
else:
    print("Sorry, Try next time")