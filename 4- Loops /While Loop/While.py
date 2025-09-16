# x = int(input("enter x: "))
# cnt = 3
# while cnt <= x:
#     if cnt % 3 == 0:
#         print(cnt)
#     cnt += 3

# 2 ** 5 

# num , pow = map(int, input("enter num & pow: ").split())
# power = 1 

# while pow > 0:
#     power *= num 
#     pow -= 1

# print(power)


# num = int(input("enter number: "))
# cnt = 0

# if num == 0 : 
#     inc = 1
# else :
#     inc = 0
#     if num < 0:
#         num = -num 
#     cnt = num 
#     while cnt > 0:
#         cnt //= 10
#         inc += 1

# print("number of digits",num,"is: ", inc) 

# *
# **
# ***
# ****
# *****


# num = int(input("enter x: "))
# T = 0 
# while T < num :

#     lo = 0 
#     while T >= lo:
#         print("*",end="")
#         lo += 1
#     print()
#     T+=1  

# While Loops Homework 1

# Homework 1: Print Range

# x , y = map(int,input("enter x & y : ").split())

# while x <= y :
#     print(x)
#     x+=1

# Homework 2: Repeat Me

# n = int(input("enter n: "))
# s = input("enter str: ")

# while n > 0 :
#     print(s,end="")
#     n-=1

# Homework 3: Print face down left angled triangle

# num = int(input("enter num : "))
 
# while num > 0:
#     s = 0 
#     while num > s:
#         print("*", end="")
#         s+=1
#     print()
#     num -= 1

# Homework 4: Special Average

# T = int(input("enter num: "))
# cnteven = 0 
# cntodd = 0
# even = 0 
# odd = 0  
# while T > 0 :
#     num = float(input("num = "))
#     if T % 2 == 0:
#         even += num 
#         cnteven += 1
#     else:
#         odd += num 
#         cntodd += 1
#     T -= 1

# print(even/cnteven , " " , odd/cntodd)


# Homework 4: Special Average (Application)

# while True:
#     print("Menu")
#     print("Enter 1 to sum numbers from 1 to N : ")
#     print("Enter 2 to evaluate simple 2 numbers expression (e.g, 2 + 3)")
#     print("Enter 3 end the program")
#     print()

#     choice = int(input("Enter choice from 1 to 3: "))
#     if choice != 1 and choice != 2 and choice != 3:
#         print('Invalid Input...Try again')
#         continue

#     if choice == 1 :
#         number = int(input("Enter a number: "))
#         sum = (number * (number + 1)) / 2 
#         print("sum from 1 to ", number ," is : ", sum)

#     elif choice == 2:
#         num1 , exp , num2= input("Enter a simple expression: ").split()
#         num1_f = float(num1)
#         num2_f = float(num2)
#         if exp == "+":
#             print("Expression value is : ",num1_f + num2_f)
#         elif exp == "*":
#             print("Expression value is : ",num1_f * num2_f)
#         elif exp == "%":
#             print("Expression value is : ",num1_f % num2_f)
#         elif exp == "/":
#             if num2 == 0:
#                 print("Sorry: No way to compute thi expression")
#             else:
#                 print("Expression value is : ", num1_f / num2_f)
#         elif exp == "**":
#             print("Expression value is : ",num1_f ** num2_f)
#     elif choice == 3 :
#         break


# While Loops Homework 3
# Homework 1: Print Diamond

# num = int(input("Enter number : "))
# row = 1 

# while num > 0:
#     col = 0 
#     while  row > col :
#         print(" ",end="")
#         col += 1

#     n = 1 
#     while (2 * n - 1) <= num :
#         print("*",end= "") 
#         n +=1
#     print()
#     num -= 1
# Homework 2: Special multiples 1
# num = int(input("Enter number: "))
# res = 0 
# while res < num:
#     if res % 8 == 0 or res % 4 == 0 and res % 3 == 0:
#         print(res , end= " ")
#     res +=1

# Homework 3: Special multiples 2

# num = int(input("enter number between 1 to 30: "))
# res = 1
# cnt = 0
# if 1 <= num <= 30:
#     while num > cnt:
#             if res % 3 == 0 and res % 4 != 0:
#                 cnt += 1
#                 print(res, end="")
#             res += 1
# else:
#     print("Please enter number between 1 to 30")

# Homework 4: Minimum of values

# T = int(input("Enter T cases: "))

# while T > 0:
#     N_T = int(input("Enter N_T: "))
#     min_num = None 
#     while N_T > 0:
#         num = int(input())
#         if min_num is None or num < min_num:
#               min_num = num
#         N_T -= 1  
#     print("Min value is :",min_num) 
#     T -= 1

# While Loops Homework 4

# Homework 1: Find NOs


# n = int(input("enter number of test cases: "))

# while n > 0:
#     str =  input("enter str: ")
#     if "NO" == str or "No" == str or "nO" == str or "no" == str or "ON" == str or "oN" == str or "On" == str or "on" == str :
#         print("match: " , str)      
#     n -= 1 

# Homework 2: Reverse number

# n = int(input("enter number: "))
# rev = 0
# while n > 0:
#     R = n % 10
#     rev = rev * 10 + R
#     n //=10 
# print(rev , rev*3)

# Homework 3: Multiplication table

# n , m = map(int,input("enter n & m : ").split())

# num1 = 1 
# while n >= num1:
#     num2 = 1
#     while m >= num2:
#         print(num1 ,"x",num2 ,"=", num1 * num2)
#         num2 += 1
#     num1 += 1 

# Homework 4: Special Sum

T = int(input("enter number of test cases : "))

while T > 0: 
    TN = int(input("enter inner test cases: "))
    step = 1
    sum = 0 
    while TN >= step:
        num = int(input("enter number: "))
        power = 1 
        count = 1
        while count <= step:
            power *= num
            count += 1
        sum += power
        step += 1
    print(sum)  
    T -= 1 
