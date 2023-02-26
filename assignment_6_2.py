# Assignment 2
# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
# You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’.
# - It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.



class Dog:
    
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
        
    def description(self):
        print(f"Name of Dog : {self.name}")
        print(f"Age of Dog : {self.age}")
        
    def get_info(self):
        print(f"coat color of Dog : {self.coat_color}")
        

class JackRussellTerrier(Dog):
    
    def __init__(self,name,age,coat_color,city,owner):
        super().__init__(name,age,coat_color)
        self.city=city
        self.owner=owner
        
    def location(self):
        print(f"location of the dog is : {self.city}")
        
    def caretaker(self):
        print(f"cartaker of the dog is : {self.owner}")

class Bulldog(Dog):
    
    def __init__(self,name,age,coat_color,food,breed):
        super().__init__(name,age,coat_color)
        self.food=food
        self.breed=breed
        
    def Food(self):
        print(f"Food of the dog is : {self.food}")
        
    def Breed(self):
        print(f"Breed of the dog is : {self.breed}")
        
        
obj=JackRussellTerrier("hardy",3,"white","Lucknow","Sam")
obj.description()
obj.get_info()
obj.location()
obj.caretaker()

obj1=Bulldog("hardy",3,"white","fish","German")
obj1.description()
obj1.get_info()
obj1.Food()
obj1.Breed()