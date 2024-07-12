str = (input())
palindrome = True
for i in range (0, len(str)):
    if str[i] != str [len(str)-i-1]:
      palindrome = False
if palindrome == True :
   print ("its a palindrome")
else:
   print("its not a palindrome")
