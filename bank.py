import sys 
class Account: 
   def __init__(self, name, balance=0.0): 
      self.name = name 
      self.balance = balance 

   def deposit(self, amount): 
      self.balance += amount 
      return self.balance 

   def withdraw(self, amount): 
      if amount >self.balance: 
         print('Balance amount is less, so no withdrawal.') 
      else:
        self.balance -= amount 
      return self.balance 


name = int(input('Enter account id:')) 
b = Account(name) 
while(True): 
   
   acc_type = input("Enter account type")
   amt = float(input('Enter balance:'))
   if choice == 'd' or choice == 'D': 
      print('Balance after deposit:', b.deposit(amt))
      print("---------------**********-------------------")
   elif choice == 'w' or choice == 'W': 
      print('Balance after withdrawal:', b.withdraw(amt))
      print("---------------**********-------------------")
