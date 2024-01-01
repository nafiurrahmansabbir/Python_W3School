class MyClass:
    x=5
# print(x)
# creating object
obj1=MyClass()
print(obj1.x)

# ....................#.........................

class Person:

    # constractor:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # str function
    # def __str__(self):
    #     return f"{self.name}({self.age})"
    
    # display
    def display(self):
        print(f"Name : {self.name} \nAge: {self.age}")

obj1=Person("Sabbir",22)
print(f"Name : {obj1.name} \nAge: {obj1.age}")

# str function
# print(obj1)

obj1.display()


