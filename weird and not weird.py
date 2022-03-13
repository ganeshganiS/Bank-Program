n=int(input("Enter n value="))
if (1<=n<=100):
    if n%2!=0:
        print("weird")
    elif 2<=n<=5:
        n%2==0
        print("Not Weird")
    elif 6<=n<=20:
        n%2==0
        print("Weird")
    elif n>20:
        n%2==0
        print("Not Weird")
else:
    print("please enter a number 1<=n<=100")
