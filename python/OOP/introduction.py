class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
person1=Person("Alice", 30)
print(person1.greet())


#2nd Example
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
car1= Car("Toyota", "Camry", 2020)
print(car1.display_info())


#3rd Example
class CAR:
    def __init__(self,brand,color,speed):
        self.brand=brand
        self.color=color
        self.speed=speed

    def drive(self):
        return f"The {self.color} {self.brand} is driving at {self.speed} mph."
    
    def repaint(self,new_color):
        self.color=new_color
        return f"The car has been repainted to {self.color}."
    

car2=CAR("Honda","Red",60)
print(car2.drive())
print(car2.repaint("Blue"))


#practice Example

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def grade(self):
        if self.marks >= 40:
            return f"{self.name} has passed with marks {self.marks}."
        else:
            return f"{self.name} has failed with marks {self.marks}."
        
    def update_marks(self,new_marks):
        self.marks=new_marks
        return f"{self.name}'s marks have been updated to {self.marks}."
    

student1=Student("Bob",101,45)
print(student1.grade())
print(student1.update_marks(35))