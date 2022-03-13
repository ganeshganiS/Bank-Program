# 1)Armstrong or Not
'''n=int(input('Enter a number='))
k=str(n)
sum=0
for i in k:
     sum=sum+int(i)**3
if(n==sum):
     print("Given number is Armstrong")
     print("The armstrong of {} is {}".format(n,sum))
else:
     print("Given number is  not a Armstrong")'''


# 2)
n=int(input('Enter a number='))
m=n
sum=0
while(n>0):
    num=n%10
    sum+=num**3
    n=n//10
    print(n)
print('sum=',sum)    
if(m==sum):
    print("Given number is Armstrong")
else:
    print("Given number is  not a Armstrong")    
    
  
