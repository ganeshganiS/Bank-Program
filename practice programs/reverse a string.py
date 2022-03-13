#program to reverse a string
name=input('Enter a name:')
print("Enetered name=",name)
#print(name[::-1])
reverse=""
for i in name:
    reverse=i+reverse
print("The reverse of a string {} is {}:".format(name,reverse))
