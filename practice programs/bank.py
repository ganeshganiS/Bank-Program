num=input("Enter the amount=")
amt=int(num)
sum=0
n=amt//2000
print("Total no of 2000's=",n)
sum=sum+n
amt=amt%2000
n=amt//500
print("Total no of 500's=",n)
sum=sum+n
amt=amt%500
n=amt//200
print("Total no of 200's=",n)
sum=sum+n
amt=amt%200
n=amt//100
print("Total no of 100's=",n)
sum=sum+n
amt=amt%100
n=amt//50
print("Total no of 50's=",n)
sum=sum+n
amt=amt%50
n=amt//20
print("Total no of 20's=",n)
sum=sum+n
amt=amt%20
n=amt//10
print("Total no of 10's=",n)
sum=sum+n
amt=amt%10
print("No of Notes=",sum)

