from teacher import Teacher 
#create instance 
t = Teacher() 
#store data into the instance 
t.setid(10) 
t.setname('Prakash') 
t.setaddress('H.No.-29, Neeruganti Street, Anantapur') 
t.setsalary(25000.50) 
#retrieve data from instance and display 
print('id=', t.getid()) 
print('name=', t.getname()) 
print('address=', t.getaddress()) 
print('salary=', t.getsalary())
