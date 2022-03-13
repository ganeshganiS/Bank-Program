a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
d=int(input("Enter d value:"))
print("Before swaping:",a,b,c,d)
e=a
a=d
d=e
e=c
c=b
b=e
print("After swaping:",a,b,c,d)
