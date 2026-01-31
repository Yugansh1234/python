x = int(input("enter the 1st cyclists speed in km per hour: "))
y = int(input("enter the 2nd cyclists speed in km per hour: "))
z = int(input("enter the 3rd cyclists speed in km per hour: "))
avg = (x+y+z)/3
if x<avg :
    print("1st cyclist is riding slower than average speed")
if y<avg :
    print("2nd cyclist is riding slower than average speed")
if z<avg :
    print("3rd cyclist is riding slower than average speed")
print("the average speed is", avg)