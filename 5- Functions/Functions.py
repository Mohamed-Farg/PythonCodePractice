# calling Built Functions

# print()

# print(1,2,'hi')

# anwser =min(3,6)

# type(15)

# len("mohamed")

# int("200")

# s1 = input()
# s2 = input("Enter: ")

# Defining our functions

# def our_print(first, second):
#     print("Sum=",first+second)
#     print("multiplication=",first* second)

# our_print(2,3)


# print("Hello")

# def our_print(first, second):
#     print("Sum=",first+second)
#     print("multiplication=",first* second)

# our_print(1 ,2 )
# print("hi")
# our_print(2,4)

# Parameter vs Argument

# def our_print(first, second):
#     # first and second is parameter
#     print("Sum=",first+second)
#     print("multiplication=",first* second)

# # first , 2*3+1 is argument
# first = 1
# our_print(first,2*3+1)

# Return Keyword 
# def our_min(first,second):
#     if first < second:
#         return first
#     return second

# def our_max(first, second):
#     if first > second:
#         return first
#     return second

# a , b = 5 ,20
# print(our_min(a,b))
# print(our_max(a,b))

# Multiple returns

# def f():
#     return 1 , 2 , 3

# a,b,c = f()

# print(type(f()))

# together = f()
# print(type(together))

# # unpack 
# x , y ,z = together

# print(x,y,z)


# my_tuple = (1,2,3)
# x,y,z = together 

# No return

# def our_print(first , second):
#     print('sum= ',first+second)
#     print("multiplication= " ,first* second)


# res = our_print( 2,3)
# # print None because function with no return 
# print(res) 


# Default Arguments 

# def my_sum(a,b,c=10,d=55):
#     return a + b + c + d

# print(my_sum(1,2,3,4)) 
# print(my_sum(1,2))


# SyntaxError
# def my_sum(a=1,b,c=3,d=3):
#     return a + b + c + d  


# calling

# def our_abs(num):
#     if num >= 0:
#         return num
#     return -num

# def our_max(first , second):
#     if first > second:
#         return first
#     return second

# print(our_max(7,4))
# print(our_max(-34,-33))
# print(our_max(6,-23))

# Enumerate Function (Built-in function)

# for item in enumerate(range(5,8)):
#     #   item is contain from 2 value first= idx ,second = value its contain (tuple) 
#     idx , value = item
#     print(idx,value)

# for idx, value in enumerate(range(5,8)):
#     print(idx,value)

# for idx, value in enumerate('ali'):
#     print(idx, value)

# Override!
# def sum(a,b):
#     return a+b

# print(sum(2,4))

# def sum(a,b,c):
#     return a+b+c

# override
# print(sum(1,2)) <---- 

# print(sum(1,2,3))

# print(len("mohamed"))

# len = 34

# # TypeError: 'int' object is not callable
# print(len("mohamed"))

# Local and Global Scope

# Local vs Global

# globl = 20 

# def f():
#     locl = 30 
#     print(locl)
#     print(globl)
#     return locl
# f()

# print(globl)

# print(locl)

# Conflicts
# b here is global value 
# b = 20
# c = 6

# def f():
#     #  b is local value
#     b = c + 1 
#     print(b)
#     return b 

# f()
# # b is global value 
# print(b)

# b = f()
# # print value b  = 7 
# print(b)


# global keywoed

# b = 20 
# c = 6 

# def f():
#     # b here is global value
#     global b
#     b = c + 1 
#     print(b)
#     return b 

# f()
# b is global value 
# print(b)

# Constants


#  global value here use a constant variable
# PI = 3.14

# def compute_area(radius):
#     return PI * radius * radius

# compute_area(5)

# Name binding

# my_str = "mohamed"

# my_str = "ahmed"

# another_str = my_str

# third_str = "mohamed"

# Unbound

# x = 10 

# def f1():
#     x = 1 
#     print(x)

# def f2():
#     print(x)

# def f3():
#     print(y)

# def f4():
#     print(y)
#     y = 2

# def f5():
#     print(x)
#     x = 2 

# def f6():
#     x = x + 1

# def f7():
#     x += 1

# def f8():
#     global x 
#     x += 1  
#     print(x)
#     return x 

# f8()

# Positional or Keyword

# def f(a ,b,c,d,e=10):
#     print(a,b,c,d,e)

# # positional arguments 
# f(1,2,3,4,5)

# #  keyword arguments
# f(a=1,b=2,c=3,d=4,e=5)
# f(e=5,b=2,c=3,d=4,a=1)

# f(1,2,c=3,d=4,e=5)
# f(1,2,c=3,d=4)

# # positional /
# def f2(x,/):
#     return x + 1

# f(10)

# Positional only
# def f3(x,/,y):
#     return x * y

# f3(1,2)
# f3(1,y=10)

# TypeError: f3() got some positional-only arguments passed as keyword arguments: 'x'
# f3(x=1,y=2)

# Keyword only *
# def f3(x,*,y):
#     return x * y

# # TypeError: f3() takes 1 positional argument but 2 were given
# f3(1,2)
# f3(1,y=3)
# f3(x=1,y=4)

# Function Homework 1

# Homework 1: Special Multiplication

# def special_multiplication(string):
#     str = ""
#     for idx , char in enumerate(string,start=1):
#         str += idx * char
#     return str
    
# my_str = input("Enter str : ")
# print(special_multiplication(my_str))

# Homework 2: Max of 6 numbers

# def my_max2(a,b):
#     if a > b:
#         return a
#     return b 

# def my_max3(a,b,c):
#     return max(my_max2(a,b),c)

# def my_max4(a,b,c,d):
#     return max(my_max3(a,b,c),d)

# def my_max5(a,b,c,d,e):
#     return max(my_max4(a,b,c,d),e)

# def my_max6(a,b,c,d,e,f):
#     return max(my_max5(a,b,c,d,e),f)

# print(my_max6(1,2,3,6,4,44))

# Homework 3: Get nth-prime

# def is_prime(num):
#     if num <= 1:
#         return False 

#     for i in range(2, num):
#         if num % i == 0:
#             return False  
#     return True  
        

# def nth_prime(n):
#     cnt = 0
#     for i in range(2, 100):  
#         if is_prime(i):
#             cnt += 1
#             if cnt == n:
#                 return i

# for i in range(1,10):
#     print(i,nth_prime(i))



# Homework 4: Get nth-fibonacci
# def nth_fib(n):
 
#     if n == 1:
#         return 0 
#     if n == 2:
#         return 1 
    
#     a,b = 0,1
#     n -= 2 

#     while n > 0:
#         c = a + b 
#         a = b 
#         b = c 
#         n -= 1 
#     return c 
# for i in range(1,10):
#     print(i,nth_fib(i))

# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 


# Function Homework 2
# Recall: Special Calculator 

def print_menu():
        while True:

            print('\n\nMenu:')
            print("Enter 1 to sum numbers from 1 to N.")
            print("Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)")
            print("Enter 3 to end the program.")
            print()

            choice = int(input("Enter choice from 1 to 3: "))
            if choice != 1 and choice != 2 and choice != 3:
                print('Invalid Input...Try again')
                continue
            else:
                return choice
                    

def sum_1_to_n():
    number = int(input("Enter a number: "))
    sum_1ton = (number * (number + 1)) // 2 
    print("Sum from 1 to",number,"is", sum_1ton)  


def divide(num1,num2,operation):
        if num2 == 0 :
            result = None
        elif operation == "/":
             result = num1 / num2
        else:
             result = num1 // num2
            
        return result

def expression():
    num1,exp,num2 = input("Enter a simple expression: ").split()
    num1,num2= float(num1),float(num2)
     
    if exp == "+":
        result = num1 + num2
    elif exp == "-":
        result = num1 - num2
    elif exp == "*":
        result = num1 * num2
    elif exp == "**":
        result = num1 ** num2
    else: 
        result = divide(num1, num2 , exp)
         
    if result != None:
        print('Expression value is ', result)
    else:
        print('Sorry: No way to compute this expression')

def calculator_interface():
    while True:
        choice = print_menu()

        if choice == 1:
            sum_1_to_n() 
        elif choice == 2:
            expression()
        else:
             break


calculator_interface()