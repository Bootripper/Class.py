input=int(input("Please enter your marks: "))
if (input>=800):
    print("First Division")
elif (input>=600) and (input<=799):
    print("Second Divison")
elif (input>=500) and (input<=599):
    print("Third Division")
else:
    print("Failed")