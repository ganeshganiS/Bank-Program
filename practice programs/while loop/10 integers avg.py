m=int(input("Enter a starting number="))
count=0
sum=0
while count<=10:
    for i in range(m,m+10):
        sum+=i
        count+=1
m+=1
avg=sum/count
print(avg)
        
        
    
