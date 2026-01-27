x = int(input("enter your marks in maths: "))
y = int(input("enter your marks in english: "))
z = int(input("enter your marks in science: "))
a = int(input("enter your marks in social science: "))
b = int(input("enter your marks in english: "))
avg = (x+y+z+a+b)/5
if 91<avg:
    print("your grade is A ")
if avg<90 and 81<avg:
    print("your grade is B ")
if avg<80 and 71<avg:
    print("your grade is C ")
if avg<70 and 61<avg:
    print("your grade is D ")
if avg<60 and 51<avg:
    print ("your grade is F")
if avg<50 and avg>1:
    print("you failed")
print("your average is ", avg)