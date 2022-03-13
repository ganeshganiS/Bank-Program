Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: E:/PYTHON/call super class constructor and method.py ========
Enter two measurements: 5 6
Traceback (most recent call last):
  File "E:/PYTHON/call super class constructor and method.py", line 14, in <module>
    r = Rectangle(a, b)
  File "E:/PYTHON/call super class constructor and method.py", line 8, in __init__
    super().__init__(x)
  File "E:/PYTHON/call super class constructor and method.py", line 3, in __init__
    self.x = X
NameError: name 'X' is not defined
>>> 
= RESTART: E:/PYTHON/call super class constructor and method.py
Enter two measurements: 5 6
Area of square= 25.0
Area of rectangle= 30.0
>>> 