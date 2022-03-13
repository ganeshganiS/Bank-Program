num=int(input("Enter a number="))
month={1:"Jan",2:"feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
if 1<=num<=12:
    print(month[num])
else:
    print("Please enter a number between 1 and 12")
