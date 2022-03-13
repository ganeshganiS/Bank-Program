class Teacher: 
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
   def setsalary(self, salary): 
      self.salary = salary 
   def getsalary(self): 
      return self.salary
class Student():
   def setmarks(self, marks):
      self. marks = marks
   def getmarks(self):
    return self. marks
s = Student()
s.setid(100)
s.setname('Rakesh')
s.setaddress('HNO-22,Ameerpet, Hyderabad')
s.setmarks(970)
print('id=', s.getid())
print('name=', s.getname())
print('address=', s.getaddress())
print('marks=', s.getmarks())
