# while Loop
# pos = 0 
# while pos < 5 :
#     print(pos, end=' ')
#     pos+= 1
# print()
# # For Loop 
# for pos in range(5):
#     print(pos, end=' ')
# print()

# for pos in range(2 , 5):
#     print(pos,end=' ')

# print()

# rng = range(1, 21, 4)
# for pos in rng:
#     print(pos, end = ' ')
# print()

# Iterating backward

# for pos in range(5 , 0 ,-1):
#     print(pos , end= ' ')
# print()

# for pos in range(10 , 0 , -2):
#     print(pos , end=' ')
# print()

# for pos in range(5):
#     pass

# for pos in range(5):
#     ...


# For with string

# mystr = "Me!"

# for char in mystr:
#     print(char)


# Nested for loops

# T = int(input("enter test cases: "))

# for case in range(T):
#     n, sum = int(input("enter number: ")), 0
#     for pos in range(1,n+1):
#         sum += pos

#     print ('sum from 1 to ',n,'=',sum)


# For else

# for i in range(5):
#     print(i)
# else:
#     print("No item left..")


# for i in range(5):
#     print(i)
#     if i == 3:
#         break
# else: 
#     print(" If you break in the loop ."
#           "else is ignored")
    
# Special Sum Homework

# t_c = int(input("enter test cases: "))

# for i in range(t_c):
#     num = int(input("enter number: "))
#     sum = 0
#     for j in range(num):
#         num_j = int(input("enter number j: ")) 
#         value = 1
#         for k in range(j + 1):
#             value *= num_j
#         sum += value
#     print("sum: ", sum )

# Practice: Special Sum - using power operator

# total_cases = int(input("enter test cases: "))
# for case in range(total_cases):
#     n ,sum = int(input("enter "))
#     for pos in range(n):
#         value = int(input())
#         sum += value ** (pos + 1)
    
#     print('sum is ', sum)

# Practice: Pair of numbers
# n , m , sum = map(int,input("enter n & m & sum: ").split())
# cnt = 0

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if i + j == sum:
#             cnt += 1
# print(cnt)


# n , m , sum = map(int,input("enter n & m & sum: ").split())
# cnt = 0

# for i in range(1,n+1):
#      j = sum - i

#      if 1 <= j <= m:
#          cnt+=1
# print(cnt)


# Practice: Triples of numbers
# n , m , w = map(int,input("enter n & m & w: ").split())
# cnt = 0

# for i in range(1, n+1):
#     for j in range(i , m + 1):
#         for k in range(1,w+1):
#             if i + j <= k:
#                 cnt += 1
# print(cnt)

# Practice: Triples of numbers (faster)


# For Loops Homework

# Homework 1: Printing X


# Homework 2: Find Special Pairs
# cnt = 0
# for i in range(50 , 301):
#     start = max(70, i+1)
#     for j in range(start,401):
#         if (i+j) % 7 == 0:
#             cnt += 1

# print(cnt)

# Homework 3: Find all quadruples
# Code it once using 4 loops (very slow!)
# cnt = 0 
# for i in range(1 , 201):
#     for j in range(1 ,201):
#         for k in range(1 ,201):
#             for n in range(1 ,201):
#                 if i + j == k + n:
#                  cnt += 1

# print(cnt) 

# Code it once using 3 loops only
# cnt = 0 
# for i in range(1 , 201):
#     for j in range(1 ,201):
#         for k in range(1 ,201):
#             n = i + j - k
#             if 1 <= n <= 200:
#                  cnt += 1

# print(cnt) 

# Homework 4: Is Prime?

# n = int(input("enter number : "))
# flag = False 

# for i in range(2,n):
#             if n % i == 0:
#                 flag = True
            
# if not flag:
#      print("YES")
# else:
#      print("NO") 


# Homework 5: Print Primes

# n = int(input("enter number : "))
# for i in range(2,n+1):
#     is_ok = True
#     for j in range(2,i):
#         if i % j == 0:
#             is_ok = False
#             break
#     if is_ok:
#         print(i,end=" ")

# Homework 6: Digits sum in range

# n , a , b = map(int, input("enter n & a & b: ").split())

# cnt = 0
# for i in range(1 , n+1):
#     sum = 0 
#     tmp = i
#     num = 0
#     while tmp:
#         num = tmp % 10
#         tmp //= 10
#         sum += num
#     if a <= sum <= b:
#         cnt += i

# print(cnt)

def sum(n):
    sume = 0
    for i in range(1,n+1):
        sume += i
    print(sume)
sum(5)