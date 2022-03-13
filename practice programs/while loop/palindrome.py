n=int(input("Enter a number="))
i=n
m=0
while n!=0:
    rem=n%10
    m=m*10+rem
    n=n//10
if i==m:
    print(i," is a Palindrome")
else:
    print(i,"is not a Palindrome")
