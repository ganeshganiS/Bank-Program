class Student: 
   def setid(self, id): 
      self.id = id 
   def getid(self): 
      return self.id 
   def setname(self, name): 
      self.name = name 
   def getname(self): 
      return self.name 
   def setaddress(self, address): 
      self.address = address 
   def getaddress(self): 
      return self.address
   def setmarks(self, marks):
      self. marks = marks
   def getmarks(self):
      return self. marks
class Teacher:
    def setsalary(self, salary): 
      self.salary = salary 
    def getsalary(self): 
      return self.salary
s = Student()
s.setid(100)
s.setname('Rakesh')
s.setaddress('HNO-22,Ameerpet, Hyderabad')
s.setmarks(970)
t = Teacher()
t.setsalary(75000.00)
print('-------------Student details--------------')
print('id=', s.getid())
print('name=', s.getname())
print('address=', s.getaddress())
print('marks=', s.getmarks())
print('-------------Teacher details----------------')
print('Teacher Salary=',t.getsalary())
