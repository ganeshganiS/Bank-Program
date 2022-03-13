n=int(input("Enter a number="))
i=n
sum=0
m=str(n)
a=len(m)
while n!=0:
    rem=n%10
    sum+=rem**a
    n=n//10
if i==sum:
    print(i," is a strong number")
else:
    print(i," is not a strong number")
