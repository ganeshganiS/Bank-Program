class Father:
   def __init__(self):
       self.property = 800000.00
   def display_property(self):
       print('Father\'s property=', self.property)
class Son(Father):
   def __init__(self):
       self.property = 200000.00
   def display_property(self):
       print('Child\'s property=', self.property)
s = Son()
s.display_property()
