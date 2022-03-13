num=int(input("Enter a number="))
week={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
if 1<=num<=7:
    print(week[num])
else:
    print("Please enter a number between 1 and 7")
