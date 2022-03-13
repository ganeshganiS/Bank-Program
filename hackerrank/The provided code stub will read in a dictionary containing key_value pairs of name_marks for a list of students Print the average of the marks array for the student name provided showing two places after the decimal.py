'''n=int(input("Enter a number="))
student_marks={}   # create a empty dictionary
for i in range(n): # 0,1,2,........,n-1
    line = input("Enter the name and marks=").split()  # here we split the input by spaces
    name, scores = line[0], line[1:]  # here 0 index as name & from the 1st index are marks
    scores = map(float,scores) #here we are converting list into map & integer to float
    student_marks[name]=scores
Required_name = input("Enter a name=0")
marks=0
for i in student_marks[Required_name]:
    marks=marks+i
Average = marks/3
print("The average value is=%.2f"%Average)'''


countries=["USA","INDIA","GERMANY","FRANCE"]
cities=["Washington","New Delhi","Berlin","Paris"]
z=zip(countries,cities)
d=dict(z)
print('{:15s}-{:15s}'.format('COUNTRY','CAPITAL'))
for k in d:
    print("{:15s}-{:15s}".format(k,d[k]))
                             
    
    
    
    
