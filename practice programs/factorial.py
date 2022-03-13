#factorial program
n=int(input("Enter a number="))
if(n>0):
    fac=1
    for i in range(1,n+1):
        fac*=i
    print("The factorial of {} is {}:".format(n,fac))
elif(n==0):
    print("The factorial of 0 is 1")
else:
    print('Please enter the number >=0')
