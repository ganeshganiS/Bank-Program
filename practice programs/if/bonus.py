salary=float(input("Enter the salary="))
Exp=int(input("Enter the employee experience="))
if Exp>5:
    salary+=salary*0.05
    print(salary)
else:
    print("The salary is {}".format(salary))
    
    
