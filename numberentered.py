number = int(input("enter a number: "))
temp = number 
count = 0
while temp!= 0:
    temp = temp // 10
    count = count + 1
print("total number of digitd in a number is", count)