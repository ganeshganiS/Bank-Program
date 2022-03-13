amount=int(input("Enter an amount="))
if amount>1000:
    amount=amount-amount*0.1
    print(amount)
else:
    print("The bill is {}".format(amount))
    
