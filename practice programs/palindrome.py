#program to check weather the string is palindrome or not
name=input('Enter a name:')
print("Enetered name=",name)
#print(name[::-1])
reverse=""
for i in name:
    reverse=i+reverse
print("The reverse of a string {} is {}".format(name,reverse))
if name==reverse:
    print("Given name is palindrome")
else:
    print("Given name is not a palindrome")
