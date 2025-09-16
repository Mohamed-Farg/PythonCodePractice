# # selection 

# salary = int(input("Enter your salary: "))
# if salary < 5000:
#     print("High salary")


# sal = int(input("Enter your salary: "))
# if sal < 5000:
#     print("High salary")
#     print("You are eligible for a bonus")

# if int(input("Enter your salary: ")) < 5000:
#     x = 10 

# print (x)  # This will raise an error if the previous input was not executed due to the condition not being met

# the if - elif chain

# sal = int(input("Enter your salary: "))
# if sal < 5000:
#     print("medium salary")
# elif sal < 10000:
#     print("High salary")


# how many digits ?

# num = int(input("Enter a number: "))
# if num < 10:
#     print("1 digit")
# elif num < 100:
#     print("2 digits")
# elif num < 1000:
#     print("3 digits")
# elif num < 10000:
#     print("4 digits")
# else:
#     print("5 or more digits")

# num = int(input("Enter a number: "))

# if 100 <= num <= 200:
#     print("The number is between 100 and 200")

#     if num % 2 == 0:
#         print("The number is even")

#         if num == 150:
#             print("The number is exactly 150")
#     else:
#         print("The number is odd")
# else:
#     print("The number is not between 100 and 200")


# num1 , operator, num2 = input("Enter two numbers and an operator (e.g., 5 + 3): ").split()

# num1 = float(num1)
# num2 = float(num2)

# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Error: Invalid operator"

# print(result)

# 
# num1, num2 = input("Enter two numbers separated by a space: ").split()
# min = num1  
# if num1 > num2:
#     min = num2

# print(min)

# num1, num2 , num3 = input("Enter two numbers separated by a space: ").split()
# min = num1  
# if num1 > num2:
#     min = num2
# if num2 > num3:
#     min = num3 
# print(min)

#  is even? print digits 
# n = int(input("Enter a number: "))

# is_even = n % 2 == 0
# if is_even :
#     print(n % 10)
# else:
#     if n < 1000 :
#       print(n % 100)
#     elif n < 1000000:
#        print(n % 10000)
#     else:
#        print(-n)

#  last 3 digits!
# n = int(input("Enter a number: "))
# if n < 10000:
#     print("Small number")
# else:
#     ls1 = n % 10 
#     n //= 10
#     ls2 = n % 10
#     n //= 10
#     ls3 = n % 10
#     n //= 10
#     sum_ls_1_2_3 = ls1 + ls2 + ls3 

#     is_even_ls1 = ls1 % 2 ==  0
#     is_even_ls2 = ls2 % 2 ==  0
#     is_even_ls3 = ls3 % 2 ==  0

#     is_even = sum_ls_1_2_3 % 2 == 0 


#     if not is_even:
#         print("Great number")
#     elif is_even:
#         if is_even_ls1 or is_even_ls2 or is_even_ls3:
#             print("Good number")
#         else:
#             print("Bad number")

# Selection Homework 1
# Homework 1: Arithmetic
# a ,b = map(int,input().split())
# is_even_a = a % 2 == 0 
# is_even_b = b % 2 == 0 

# if not is_even_a and not is_even_b :
#     print(a * b)
# elif is_even_a and is_even_b :
#     if b != 0 :
#         print(a // b)
# elif not is_even_a and is_even_b:
#     print(a + b)
# else:
#     print(a - b)

# Homework 2: Sort 3 numbers

# num1 , num2 , num3 = map(int, input("Enter 3 numbers: ").split())

# if num1 > num2:
#     temp = num1
#     num1 = num2
#     num2 = temp 
# if num1 > num3:
#     temp = num1
#     num1 = num3
#     num3 = temp 
# if num2 > num3:
#     temp = num2 
#     num2 = num3
#     num3 = temp

# print(num1 , num2 , num3)

# Homework 3: Maximum but constrained

# a , b, c  = map(int, input("Enter 3 numbers: ").split())

# res = -inf 

# if res < a < 100:
#     res = a 
# if res < b < 100:
#     res = b
# if res < c < 100:
#     res = c 

# print(res)

# Homework 4: Conditional Count

# x = int(input("enter number: "))
# a1,a2,a3,a4,a5 = map(int,input("enter 5 numbers: ").split())

# cnt = 0 

# cnt += a1 <= x
# cnt += a2 <= x
# cnt += a3 <= x
# cnt += a4 <= x
# cnt += a5 <= x

# print (cnt, "  " , 5 - cnt)

# Selection Homework 2

# Homework 1: Find Maximum of 10 numbers

# result = float(input())

# num = float(input())
# if result < num :
#     result = num

# num = float(input())
# if result < num :
#     result = num

# num = float(input())
# if result < num :
#     result = num

# num = float(input())
# if result < num :
#     result = num

# num = float(input())
# if result < num :
#     result = num

# num = float(input())
# if result < num :
#     result = num

# num = float(input())
# if result < num :
#     result = num

# num = float(input())
# if result < num :
#     result = num

# num = float(input())
# if result < num :
#     result = num

# print(result)

# Homework 2: Find Maximum up to 10 numbers

# cnt = int(input())

# res  = float(input())
# cnt -=1

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res =num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res =num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res =num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res =num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res =num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res =num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res =num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > res:
#         res =num

# print(res)

# Selection Homework 3
# Homework 1: Intervals
# X = int(input("enter x: "))
# S1,E1,S2,E2,S3,E3 = map(int,input("enter s & e : ").split())
# cnt = 0 

# if S1 <= X <= E1: 
#     cnt+= 1 
# if S2 <= X <= E2: 
#     cnt+=1 
# if S3 <= X <= E3: 
#     cnt+=1 

# print(cnt)

# Homework 2: Two Intervals Intersection

# S1,E1,S2,E2= map(int,input("enter s & e : ").split())

# if E1 < S2 or E2 < S1:
#     print(-1)
# else:

#     if S1 < S2 :
#         S1 = S2
#     if E1 > E2:
#         E1 = E2
#     print(S1 , E1)
