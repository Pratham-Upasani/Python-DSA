class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("A dog barks.")
        super().speak()

class Cat(Animal):
    pass

d=Dog()
d.speak()

c=Cat()
c.speak()
    
