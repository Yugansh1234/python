name = "penguin"
age = 15
is_student = True
weight = 38.5
print("name :", type(name))
print("data type of name is :", type(name))
print("age :", age)
print("data type of age is :", type(age))
print("is_student :", is_student)
print("data type of is_student is :", type(is_student))
print("weight :", weight)
print("data type of weight is :", type(weight))
print("\n after casting...")
age = str(age)
print(age)
print("data type of age is", type(age))
weight = int(weight)
print(weight)
print("data type of weight is", type(weight))
name = "YugaNsh"
print("upper case- " ,name.upper())
print("lower case- " ,name.lower())
print("length -" ,len(name))
print("slicing -", name[1:3])
print("first letter-", name[0])
print("last letter-", name[-1])
print("reverse", name[::-1])
print("joining of two strings ", "hello"+ name)
a = "welcome"
print(name+" "+a)