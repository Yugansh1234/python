x = str(input("enter a word: "))
y = str(input("enter a letter whose number of times repeated in the above word you want to know: "))
i = 0
count = 0
while(i < len(x)):
    if(x[i] == y):
        count = count + 1
    i = i + 1
print("the total number of times", y, "has occured is", count)
