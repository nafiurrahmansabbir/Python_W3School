# parent class
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def display(self):
        print(f"{self.fname} {self.lname}")

# obj1=Person("sabbir", "Rahman")
# obj1.display()

# child Class 
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    
obj1=Student("sabbir", "Rahman")
obj1.display()
