class BankAccount:
  def __init__(self,balance,name,post):
    self.__balance=balance  #Private variable
    self._name=name #Protected variable
    self.post=post #Public variable(default)

@property  #(Built in decorator to set any method as a getter method i.e. read only method, allowing it to act like an attribute)
def balance(self):
  return self.__balance

@balance.setter #(It is used to set a method as setter only method, on which we applied @property.)
def balance(self,amount):
  if amount<0:
    print("Balance cannot be -ve")
  else:
    self.__balance=amount

b=BankAccount(50000,"Rajesh","Accountant")
print(b.balance)  #Automatically calls getter method, allowing balance() to act like an attribute instead of a method
b.balance=4000 #Automatically calls setter method, allowing us to control access to private variables
