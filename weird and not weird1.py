n=int(input("enter a number"))
if 1<=n<=100:
    if n%2!=0 or (n%2==0 and 6<=n<=20):
        print("Weird")
    elif n%2==0 and (2<=n<=5 or n>20):
        print("Not Weird")
else:
    print("Please enter the value between 1 to 100")
