print("select your ride")
print("1 = car")
print("2 = bike")
x = int(input("enter your choice "))
if x == 1:
    print("please select your car ")
    print("1 = ecocar")
    print("2 = petrolcar")
    y = int(input("enter your choice "))
    if y == 1:
        print("you selected ecocar ")
    else:
        print("you selected petrolcar")
else:
    print("please select your bike ")
    print("1 = ecobike")
    print("2 = bike")
    z = int(input("enter your choice "))
    if z == 1:
        print("you selected ecobike")
    else:
        print("you selected bike")
