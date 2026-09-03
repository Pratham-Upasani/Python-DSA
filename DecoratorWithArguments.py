#A decorator is a function that is used to extend another function without modifying the base function itself.
#It takes another function as an argument, to extend(decorate) its original definition
#To apply decorator on a base function that accepts parameters, we must add *args and **kwargs to the inner function as well as func() itself inside the decorator's definition

def add_sprinkles(func):   #Defining the decorator named add_sprinkles
  def wrapper(*args,**kwargs):   #We must add *args,**kwargs here to accept parameters from the base function 
    print("After adding sprinkles.")
    func(*args,**kwargs)    #Now passing *args,**kwargs to the base function
  return wrapper

@add_sprinkles      #Applying the decorator to the base function
def get_icecream(flavour):
  print(f"Here is your {flavour} ice cream")

get_icecream("Vanilla")   #Calling the base function, giving an argument to it

#output
After Adding sprinkles.
Here is your Vanilla ice cream
