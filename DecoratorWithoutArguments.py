#A decorator is a function that is used to extend another function without modifying the base function itself.
#It takes another function as an argument, to extend(decorate) its original definition
#To apply decorator on a function, we use @decorator_name before the base function to decorate it
#We must use another inner function(that defines what the decorator will do) inside the decorator and return it
#Otherwise, the decorator will run without even calling the base function(as soon as we apply it

def add_sprinkles(func):   #Defining the decorator named add_sprinkles
  def wrapper():   #We must define an inner function inside decorator & return it to prevent auto-calling the decorator on applying
    print("After adding sprinkles.")
    func()
  return wrapper

@add_sprinkles     #Applying the decorator to the base function
def get_icecream():
  print("Here is your ice cream")

get_icecream()   #Calling the base function

#output
After Adding sprinkles.
Here is your ice cream
