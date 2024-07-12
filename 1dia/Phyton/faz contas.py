number = 1*1
x = int(input("1 x 1 = "))
i = 0
if x == number:
    print ("you are correct")
    i = i+1
else:
    print ("you are wrong")
number = 1+9
y = int(input("1 + 9 = "))
if y == number:
    print ("you are correct")
    i = i+1
else:
    print ("you are wrong")
number = 9+8
z = int(input("9 + 8 = "))
if z == number:
    print ("you are correct")
    i = i+1
else:
    print ("you are wrong")
number = 4+2
a = int(input("4 + 2 = "))
if a == number:
    print ("you are correct")
    i = i+1
else: 
    print ("you are wrong")
number = 2*4
b = int(input("2 x 4 = "))
if b == number:
    print ("you are correct")
    i = i+1
else:
    print ("you are wrong")
print (f"you scored {i}")