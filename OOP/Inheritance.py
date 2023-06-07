class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet): #Now this can inherit parent class functions
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    
    def speak(self):
        print("meow")

class Dog(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    
    def speak(self):
        print("bark")

p = Pet("gaven", 21)
p.show()
d = Dog("Kanon", 20)
d.show()
c = Cat("Kanon2", 20)
c.show()