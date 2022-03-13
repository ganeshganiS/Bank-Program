number = int(input(" Please Enter any  Integer : "))

if((number % 5 == 0) and (number % 11 == 0)):
    print("Given Number {0} is Divisible by 5 and 11".format(number))
else:
    print("Given Number {0} is Not Divisible by 5 and 11".format(number))
