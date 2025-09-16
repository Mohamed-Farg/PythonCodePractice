# Define a class ... Create an Object


# class Emp: 
#     name = None
#     salary = None
#     address = None


# Emp1 = Emp()
# Emp1.name = "mohamed ahmed"
# Emp1.salary = 10000
# Emp1.address = "cairo, Egypt"

# print(Emp1.name, Emp1.salary, Emp1.address)


# Creating multiple objects


# Emp1 = Emp()
# Emp1.name = "ahmed farg"
# Emp1.salary = 1000
# Emp1.address = "cairo, Egypt"

# print(Emp1.name, Emp1.salary, Emp1.address)


# Emp2 = Emp()
# Emp2.name = "mohamed ahmed"
# Emp2.salary = 10000
# Emp2.address = "cairo, Egypt"

# print(Emp2.name, Emp2.salary, Emp2.address)

# Methods


# Functions with Objects

# class Emp: 
#     name = None
#     salary = None
#     address = None

# function 

# def print_empl(Obj):
#     print("Employee name",Obj.name)
#     print("Employee salary",Obj.salary)
#     print("Employee address",Obj.address)


# Empl = Emp()
# Empl.name = "mohamed ahmed"
# Empl.salary = 10000
# Empl.address = "cairo, Egypt"

# print_empl(Empl)

# Read and Write

# class Emp: 
#     name = None
#     salary = None
#     address = None

# def print_empl(Obj):
#     print("Employee name",Obj.name)
#     print("Employee salary",Obj.salary)
#     print("Employee address",Obj.address)

# def read_empl():
#     Obj = Emp()
#     Obj.name = input("Enter name: ")
#     Obj.salary = float(input("Enter salary: "))
#     Obj.address = input("Enter address: ")

#     return Obj

# read_emp = read_empl()
# print_empl(read_emp)



# Methods

# class Emp: 
#     name = None
#     salary = None
#     address = None

#     def print(self):
#         print("Employee name",self.name)
#         print("Employee salary",self.salary)
#         print("Employee address",self.address)

#     def read_empl(self):
#         self.name = input("Enter name: ")
#         self.salary = float(input("Enter salary: "))
#         self.address = input("Enter address: ")


# obj = Emp()
# obj.read_empl()
# obj.print()

# Constructor

# Using Constructor

# class Emp:
#     def __init__(self,name,salary,address):
#         self.name = name
#         self.salary = salary
#         self.address = address 
    
#     def print(self):
#         print("Employee name",self.name)
#         print("Employee salary",self.salary)
#         print("Employee address",self.address)
        

# obj = Emp("mohamed ahmed" , 1231 , "cairo")
# obj.print()

# Class of Class

# class FullName:
#     def __init__(self,firt_name,last_name):
#         self.firt_name = firt_name
#         self.middle_name = None
#         self.last_name = last_name


# class Emp():

#     def __init__(self,firt_name,last_name , salary , address):
#         self.full_name = FullName(firt_name,last_name)
#         self.salary = salary 
#         self.address = address

#     def print(self):
#         print("Employee name",self.full_name.firt_name + " " +
#               self.full_name.last_name)
#         print("Employee salary",self.salary)
#         print("Employee address",self.address)

# obj = Emp("mohamed", "ahmed" , 1231 , "cairo")
# obj.print()

        
# str and repr for Class

# Dunder init

# class emp:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# obj = emp("mohamed",29)
# print(obj)


# Dunder str

# class emp:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return 'employee ' + self.name + ' is ' + str(self.age) + ' years old'
    
# obj = emp("mohamed",29)
# print(obj)
# print(obj.__str__())

# Dunder str: must return string

# class emp:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return 'employee ' + self.name + ' is ' + str(self.age) + ' years old'
    
# obj = emp("mohamed",29)
# print(str(obj))
# print(obj)

# print(obj.__str__()) 


# Dunder repr


# class emp:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return 'employee ' + self.name + ' is ' + str(self.age) + ' years old'
    
#     def __repr__(self):
#         return 'employee ' + self.name + ' is ' + str(self.age) + ' years old' + ' **' 
    
    
# obj = emp("mohamed",29)

# print(obj)

# print(str(obj))
# print(repr(obj))
# print(obj.__repr__()) 
# print(obj.__str__())

# Class Homework 1


# Rectangle and Circle

# class rectangle:
#     def __init__(self,width, height):
#          self.width = width
#          self.height = height

#     def get_area(self):
#         return self.width * self.height


# class circle:
#     PI = 3.14 
#     def __init__(self,radius):
#        self.radius = radius

#     def get_area(self):
#         return self.PI * (self.radius ** 2)
    

# r = rectangle(2,5)
# print(r.get_area())


# c = circle(5)
# print(c.get_area())


# Editor (Rectangle and Circle)


# class rectangle:
#     def __init__(self,width, height):
#          self.width = width
#          self.height = height

#     def get_area(self):
#         return self.width * self.height


# class Circle:
#     PI = 3.14 
#     def __init__(self,radius):
#        self.radius = radius

#     def get_area(self):
#         return self.PI * (self.radius ** 2)
    

# class Editor:
#     def __init__(self):
#         self.rect = None
#         self.circle = None

#     def create_rectangle(self,width, height):
#         self.rect = rectangle(width,height)

#     def create_circle(self, radius):
#         self.circle = Circle(radius)

#     def change_rectangle(self,factor):
#         if self.rect == None:
#             return
        
#         width , height = self.rect.width + factor , self.rect.height + factor
#         self.create_rectangle(width,height)

#     def change_circle(self,factor):
#         if self.circle == None:
#             return
        
#         self.create_circle(self.circle.radius + factor)

#     def change (self, factor):
#         self.change_rectangle(factor)
#         self.change_circle(factor)

#     def print(self):
#         if self.rect != None:
#             print('Rectangle area', self.rect.get_area())

       
#         if self.circle != None:
#             print('circle area', self.circle.get_area())

# editor = Editor()
# editor.create_rectangle(3, 5)
# editor.create_circle(5)
# editor.print()
# #Rectangle area 15
# #Circle area 78.5
# editor.create_circle(5)
# editor.change(2)
# editor.print()
#Rectangle area 35
#Circle area 153.86


# Class Homework 2

# Homework 1: Our MyRange Class


# class MyRange:
    
#     def __init__(self,start, end ,step):
#         self.start = start
#         self.end = end 
#         self.step = step


#     def has_next(self):
#         return self.start < self.end 
        
#     def get_next(self):
#         ret = self.start
#         self.start += self.step
#         return ret

# rng = MyRange(5,10,1)

# while rng.has_next():
#     print(rng.get_next(), end=' ')

# print()

# rng = MyRange(5,10,2)

# while rng.has_next():
#     print(rng.get_next(), end=' ')
        

# Homework 2: Our MyRange Class (Flexible)


class MyRange:
    
    def __init__(self,start, end ,step):
        self.start = start
        self.end = end 
        self.step = step
        self.idx = 0


    def has_next(self):
        if self.step > 0 :
            return self.start < self.end 
        return self.start > self.end 
        
    def get_next(self):
        ret = self.idx , self.start
        self.start += self.step
        self.idx +=1 
        return ret

rng = MyRange(10,5,-1)

while rng.has_next():
    print(rng.get_next(), end=' ')

print()

rng = MyRange(5,10,2)

while rng.has_next():
    print(rng.get_next(), end=' ')


