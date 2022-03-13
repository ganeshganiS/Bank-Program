n=int(input("Enter a number="))
if 1<=n<=100:
    if (n%2==0) and (2<=n<=5 or n>20):
         print("Not weird")
    elif (n%2!=0) or (n%2==0 and 6<=n<=20):
         print("Weird")
else:
    print("Please enter a number between 1 and 100") 
    
