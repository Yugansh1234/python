amount = int(input("enter the amount: "))
note_1 = amount//100
print("value of ", note_1)
note_2 = (amount%100)//50
print  ("value of ", note_2)
note_3 = ((amount%100)%50)//10
print  ("value of ", note_3)
print("notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)