from abc import ABC, abstractmethod

class TaskBase(ABC):
    total_tasks=0

    def __init__(self,name,priority):
        self.name=name
        self.priority=priority
        self.__status="Pending"
        TaskBase.total_tasks+=1

    @abstractmethod
    def details(self):
        pass

    @property
    def status(self):
        return f"Current status = {self.__status}"

    @status.setter
    def status(self,value):
        valid_status = ["Pending","In progress","Done"]
        if value in valid_status:
            self.__status=value
        else:
            raise ValueError("Invalid value for status.")

    def __lt__(self,other):
        return self.priority < other.priority

    def __str__(self):
        return f"[{self.__status}] Buy groceries (priority {self.priority})"

    @classmethod
    def get_total_tasks(cls):
        return cls.total_tasks

    @staticmethod
    def is_valid_priority(p):
        if p in [1,2,3,4,5]:
            return True
        else:
            return False

class RegularTask(TaskBase):
    def details(self):
        return f"Regular task: {self.name}"

    @classmethod
    def quick_task(cls,name):
        return cls(name,1)

class UrgentTask(TaskBase):
    def __init__(self,name,priority,deadline):
        super().__init__(name,priority)
        self.deadline=deadline
        
    def details(self):
        return f"URGENT: {self.name} - due {self.deadline}!"

r1=RegularTask("Pratham",2)
r2=RegularTask.quick_task("Samarth")
u1=UrgentTask("Rishabh",4,2)
u2=UrgentTask("Rahul",5,1)

L=[r1, r2, u1, u2]  #List of all tasks

for x in L:
    print(x.details())

for x in L:
    print(str(x))
 
r1.status="Done"
print(r1.status)

#r2.status="Jack"   #Just to check the @status.setter method

#Lower number = higher priority(sort the list according to priority using __lt__ method)
#sort() method internally uses __lt__ when comparing values
L.sort()  #And it also sorts the list inplace

for x in L:
    print(str(x))

print(TaskBase.get_total_tasks())  #Testing class method
print(TaskBase.is_valid_priority("Jackkk"))  #Testing static method

#Confirm Abstraction
t=TaskBase("Raj",20)
        
        
    

        
 
        
