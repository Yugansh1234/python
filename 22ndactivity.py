x = int(input("how many electricity units consumed: "))
if x>=50 and x<0:
    print("cost = ",x * 2.60 + 25)
elif 50>x and x<=100:
    print("cost = ",x * 3.25 + 30)
elif 100<x and 200>=x:
    print("cost = ",x * 5.26 + 45)
elif x>200:
    print("cost = ",x * 8.45 + 75)
else:
    print("error units too much or too less")