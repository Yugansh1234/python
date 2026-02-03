x = str(input("do you have a medical cause: "))
if x == "yes":
    print("you are allowed to give the exam ")
else:
    y = int(input("enter your attendance: "))
    if y >= 75:
        print("you are allowed to give the exam")
    else:
        print("you are not allowed to give the exam")