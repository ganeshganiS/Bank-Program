n=int(input('Enter n value:'))
product=1
for i in range(1,n+1):
    product*=i
print('The product of 1 to {} is {}'.format(n,product))
