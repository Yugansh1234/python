ch = input("please enter your own character: ")

if((ch >= 'a' and ch<= 'z') or (ch>= 'A' and ch<= 'Z')):
    print("the given charcter", ch, "is an alphabet")
else:
    print("the given charcter", ch, "is not an alphabet")