a=int(input("Enter number of classes held="))
b=int(input("Enter number of classes attended="))
c=(b/a)*100
print(c)
if c>=75:
    print("Allowed to Exam hall")
else:
    print("Not allowed to sit in the exam hall")
