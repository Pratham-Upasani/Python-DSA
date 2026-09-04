#Polymorphism using method overriding
class Animal:
    def speak(self):
        print("Animal speaks.")

        
class Dog(Animal):
    def speak(self):
        print("A dog barks")

        
class Cat(Animal):
    def speak(self):
        print("A cat meows")

        
L=[Dog(),Cat(),Animal()]
for x in L:
    x.speak()
