# class Car: #Uppercase letter for Classes

#     def __init__(self, name, size): #This initializes and helps sets up chracteristics
#         self.name = name
#         self.size = size
#         #So, __init__ is like the special function that sets up the initial state of an object, just like getting a toy car ready to play with.
    
#     def model(self): #Method, define methods of what functions do
#         print("Honda") #Method is a function in class

#     def color(self):
#         print("Black")
    
#     def set_name(self, name):
#         self.name = name

# c = Car("Mine", "Big")
# c.set_name("Bigger")
# print(c.name)



class Kid:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
    def set_name(self, name):
        self.name = name

k = Kid("gaven", 21)
print(k.get_name())
k.set_name("Kanon")
print(k.get_name())
