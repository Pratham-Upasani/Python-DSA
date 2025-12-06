try:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("The division of both numbers is: ",(x/y))
    
except  ZeroDivisionError:
    print("You cannot divide a number by zero!")

except TypeError:
    print("Please enter a number!")

except Exception:
    print("Some error occured!")

else:
    age=int(input("Enter your age: "))

    if age<0:
        raise ValueError("Age is invalid!")
    else:
        print("You are ",age," years old!")

finally:
    print("This message will always print regardless of an error or not")


    
    
    
