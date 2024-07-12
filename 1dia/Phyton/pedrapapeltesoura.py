from random import randint
x = randint(1, 3)
print (f"chose:\n1) rock\n2) paper\n3)scissors")
number = int(input())
if number == 1 and x == number:
    print ("you chose the same as the computer \nyou tied")
elif number == 1 and x == 2: 
    print ("you chose rock \n the computer chose paper \nyou lost")
elif number == 1 and x == 3:
    print ("you chose rock \nthe computer chose scissors\nyou win")
elif number == 2 and x == 1:
    print ("you chose paper \nthe computer chose rock \nyou win")
elif number == 2 and x == number:
    print ("you chose the same as the computer \nyou tied")
elif number == 2 and x == 3:
    print ("you chose paper \nthe computer chose scissors \nyou lost")
elif number == 3 and x == 1:
    print ("you chose scissors \nthe computer chose rock \nyou lost")
elif number == 3 and x == 2:
    print ("you chose scissors \nthe computer chose paper \nyou win")
else:
    print ("you chose the same as the computer \nyou tied")