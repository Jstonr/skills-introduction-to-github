from abc import ABC, abstractmethod
import math

#Classes & Objects
class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        return f"Student name: {self.name} of age: {self.age} years with a grade: {self.grade}%"
        
    def is_passing(self):
        return self.grade >= 50
 
if __name__ == "__main__" :
    std1 = Student("John", 25, 20)      
    std2 = Student("Job", 18, 60)
    for student in [std1, std2]:
        print(student.display_info())
        print(f"Is passing: {student.is_passing()}")
        print('×' * 23)


print(" _" *47)
#Inheritance
class Animal:
    def __init__(self, species: str, sound: str):
        self.species = species 
        self.sound = sound 
        
    def make_sound(self):
        return f"{self.species} sounds {self.sound}" 

class Dog(Animal):
    def __init__(self, species: str, sound: str, breed: str):
        super().__init__(species, sound)
        self.breed = breed
    
    def display_breed(self):
        return f"This is a {self.breed}."     
    
class Cat(Animal):
    def scratch(self):
        return "This cat is scratchy"
  
if __name__ == "__main__":
    dog = Dog("Dog", "Woof Woof", "Labrador")
    cat = Cat("Cat", "Meow")

    print(dog.make_sound())
    print(dog.display_breed())
    print("×" * 30)

    print(cat.make_sound())
    print(cat.scratch())
    print("×" * 30)
 
    
print(" _" *47)  
#Polymorphism
def play_sound(animal):
    return animal.make_sound()
    
class Bird(Animal):
   def __init__(self, species: str, sound: str, can_fly: bool):
       super().__init__(species, sound)
       self.can_fly = can_fly

   def make_sound(self):
       return f"{self.species} chirps {self.sound}"

if __name__ == '__main__':
    dog = Dog("Skubi", "wuffwuff", "mutina")
    cat = Cat("White", "miauu")   
    bird = Bird("Parrot", "tweet", True)
    for animal in [dog, cat, bird]:
        print(play_sound(animal))
        print("×"*30)
    
  
      
print(" _" *47)    
#Encapsulation    
class BankAccount:
    def __init__(self, __account_number: int, __balance: int):
        self.__account_number = __account_number
        self.__balance = __balance
    
    def deposit(self, amount):
        self.__balance+=amount
        print(f"Deposit Successfully \nCurrent balance: {self.__balance} ")
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance-=amount
            print(f"Withdrawal Successfully \nCurrent balance: {self.__balance}")
        else:
           print(f"Insufficient funds \nCurrent balance: {self.__balance}")     
    
    def get_balance(self):
        print(f"Current balance: {self.__balance}")
    
if __name__ == "__main__":
    acc = BankAccount(1, 1000000) 
    acc.deposit(2000) 
    acc.withdraw(10000000)
    acc.withdraw(500000)
    acc.get_balance()
    
print(" _" *47)    
#Abstraction    
class Shape(ABC): 
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass  
   
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
          
    def area(self):
        return f"Rec.Area: {self.width * self.height}"
        
    def perimeter(self):
        return f"Rec.Perimeter: {2 * (self.width + self.height)}"
        
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        
    def area(self):
        return f"Cir.Area: {round(math.pi * (self.radius**2), 2)}"
       
    def perimeter(self):
        return f"Cir.Perimeter: {round(math.pi * (self.radius*2), 2)}"
        
if __name__ == "__main__":
    rec = Rectangle(9, 7) 
    cir = Circle(17)
    print(rec.area()) 
    print(rec.perimeter())
    print(cir.area())
    print(cir.perimeter())
        