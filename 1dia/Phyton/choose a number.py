from random import randint
x = randint(1, 50)
number = int(input())
print (f"chose a number: {number}")
i = 1
while x!= number:
    if x > number :
        print ("the correct number is higher")
        number = int(input())
        print (f"chose a number: {number}")
        i = i + 1 
    elif x < number:
        print ("the correct number is lower")
        number = int(input())
        print (f"chose a number: {number}")
        i = i + 1
print (f"you guessed the number in {i} tries")