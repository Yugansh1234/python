number = int(input("enter a number: "))
if number>0:
    print("number is positive")
else:
    print("number is negative")

fixedprice = int(input("enter a fixed price: "))
price = int(input("enter the price u sold for: "))
if price>fixedprice:
    print("you are in profit")
    print("you have extra ", price-fixedprice)
else:
    print("you are in loss")
    print("you have lost ", fixedprice-price)



