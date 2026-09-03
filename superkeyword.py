class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self,name,breed,gender):
        super().__init__(name)   #Calling parent class constructor and passing name to it
        self.breed=breed
        self.gender=gender

    def intro(self):
        print(f"{self.name} is a dog of breed {self.breed} and gender {self.gender}")
        super().sound()  #Calling parent class's sound() method

d=Dog("Rex","Pitbull","Male")  # "Rex" i.e. the name will be passed to parent's constructor
d.intro()
    
