# # # Arithmetic Operators
# # x = 6 
# # y = 3
# # print (x + y)  # Addition
# # print (x + 2 * y - 1)  # Addition with multiplication and subtraction
# # print (x / y)  # Division

# # z = (x + y) / 3 / 2 # Division with parentheses
# # print (z)  # Output of the division with parentheses

# # print (-z)  # Negation of z

# # #binary and unary operators
# # print (x + y)  # Binary addition
# # print (-7)  # Unary negation
# # print (--7)  # Unary negation applied twice

# # # division and floor division
# # print (x / y)  # Regular division
# # print (x // y)  # Floor division
# # # division by power of 10s
# # num = 12345

# # print (num / 1000)  # Division by 1000
# # print (num // 1000)  # Floor division by 1000

# # # power operator
# # print (2 ** 2 )  # 2 raised to the power of 2

# # # Modulus operator
# # print (x % y)  # Modulus operation

# # print (x % 2 == 0)  # Check if x is even using modulus
# # print (x % 2 != 0)  # Check if x is odd using modulus

# # # compound assignment operators
# # x += 1  # Increment x by 1
# # print (x)  # Output the new value of x
# # x -= 1  # Decrement x by 1
# # print (x)  # Output the new value of x
# # x *= 2  # Multiply x by 2
# # print (x)  # Output the new value of x
# # x /= 2  # Divide x by 2
# # print (x)  # Output the new value of x
# # x //= 2  # Floor divide x by 2
# # print (x)  # Output the new value of x
# # x **= 2  # Raise x to the power of 2
# # print (x)  # Output the new value of x
# # x %= 2  # Modulus operation on x with 2
# # print (x)  # Output the new value of x

# # multiple assignment operators
# x, y = 1, 2  # Assign 1 to x and 2 to y
# print (x, y)  # Output the values of x and y
# x, y = y, x  # Swap values of x and y
# print (x, y)  # Output the swapped values of x and y

# # operators  associativity
# # x = 1
# # y = 2
# z = 3
# # result = x + y - z  # Left to right associativity
# # print(result)  # Output the result of the left to right associativity
# # result = x + (y - z)  # Parentheses to change order of operations
# # print(result)  # Output the result with changed order of operations
# # result = (x + y) - z  # Parentheses to change order of operations
# # print(result)  # Output the result with changed order of operations
# # result = x + y * z  # Multiplication before addition
# # print(result)  # Output the result of multiplication before addition
# # result = (x + y) * z  # Parentheses to change order of operations
# # print(result)  # Output the result with changed order of operations
# # result = x + y / z  # Division before addition
# # print(result)  # Output the result of division before addition
# # result = (x + y) / z  # Parentheses to change order of operations
# # print(result)  # Output the result with changed order of operations
# # result = x + y // z  # Floor division before addition
# # print(result)  # Output the result of floor division before addition
# # result = (x + y) // z  # Parentheses to change order of operations
# # print(result)  # Output the result with changed order of operations
# # result = x + y ** z  # Exponentiation before addition
# # print(result)  # Output the result of exponentiation before addition
# # result = (x + y) ** z  # Parentheses to change order of operations
# # print(result)  # Output the result with changed order of operations

# print( x ** y ** z)  # Exponentiation with right-to-left associativity
# # print( x ** (y ** z))  # Parentheses to change order of operations
# # print( (x ** y) ** z)  # Parentheses to change order of operations

# A = B = C = 2
# print(A, B, C)  # Output the values of A, B, and C

# # order of evaluation
# x = 1
# y = 2
# z = 3
# result = x + y * z  # Multiplication before addition
# print(result)  # Output the result of multiplication before addition
# result = (x + y) * z  # Parentheses to change order of operations
# print(result)  # Output the result with changed order of operations
# result = x + y / z  # Division before addition
# print(result)  # Output the result of division before addition
# result = (x + y) / z  # Parentheses to change order of operations
# print(result)  # Output the result with changed order of operations
# result = x + y // z  # Floor division before addition
# print(result)  # Output the result of floor division before addition
# result = (x + y) // z  # Parentheses to change order of operations
# print(result)  # Output the result with changed order of operations
# result = x + y ** z  # Exponentiation before addition
# print(result)  # Output the result of exponentiation before addition
# result = (x + y) ** z  # Parentheses to change order of operations
# print(result)  # Output the result with changed order of operations 


# # RELATIONAL OPERATORS# Relational operators are used to compare two values and return a boolean result.

# # BOOLEAN DATA TYPE
# # The boolean data type can have two values: True or False.

# STATUS = True  # Assigning True to STATUS
# print(STATUS)  # Output the value of STATUS

# print(type(STATUS))  # Output the type of STATUS, which is <class 'bool'>

# print(not STATUS)  # Output the negation of STATUS, which is False

# print(bool(0))  # Output the boolean value of 0, which is False
# print(bool(''))  # Output the boolean value of an empty string, which is False
# print(bool([]))  # Output the boolean value of an empty list, which is False
# print(bool(()))  # Output the boolean value of an empty tuple, which is False
# print(bool({}))  # Output the boolean value of an empty dictionary, which is False
# print(bool(None))  # Output the boolean value of None, which is False

# print('love' == 'love')  # Output True because both strings are equal
# print('love' != 'hate')  # Output True because the strings are not equal
# print('love' < 'hate')  # Output False because 'love' is lexicographically greater than 'hate'
# print('love' > 'hate')  # Output True because 'love' is lexicographically greater than 'hate'
# print('love' <= 'hate')  # Output False because 'love' is not less than or equal to 'hate'
# print('love' >= 'hate')  # Output True because 'love' is greater than or equal to 'hate'

# print(1 + 2 == 3)  # Output True because 1 + 2 equals 3
# print(1 + 2 != 3)  # Output False because 1 + 2 does not equal 3
# print(16 == 2 ** 4)  # Output True because 16 equals 2 raised to the power of 4
# print(16 != 2 ** 4)  # Output False because 16 equals 2 raised to the power of 4
# print(16 < 2 ** 4)  # Output False because 16 is not less than 2 raised to the power of 4
# print(16 > 2 ** 4)  # Output False because 16 is not greater than 2 raised to the power of 4
# print(16 <= 2 ** 4)  # Output True because 16 is less than or equal to 2 raised to the power of 4
# print(16 >= 2 ** 4)  # Output True because 16 is greater than or equal to 2 raised to the power of 4    

# # truth table for logical operators
# # The truth table for logical operators AND, OR, and NOT is as follows:
# # AND (&&):
# # True AND True = True
# # True AND False = False
# # False AND True = False
# # False AND False = False   

# # OR (||):
# # True OR True = True
# # True OR False = True
# # False OR True = True
# # False OR False = False    

# # NOT (!):
# # NOT True = False
# # NOT False = True
# # Example of logical operators
# print(True and True)  # Output True
# print(True and False)  # Output False
# print(False and True)  # Output False
# print(False and False)  # Output False  

# print(True or True)  # Output True
# print(True or False)  # Output True
# print(False or True)  # Output True
# print(False or False)  # Output False

# print(not True)  # Output False
# print(not False)  # Output True

# # Example of logical operators with variables
# x = 5
# y = 10
# print(x > 0 and y > 0)  # Output True because both conditions are True
# print(x > 0 or y < 0)  # Output True because at least one condition is True
# print(not (x < 0))  # Output True because x is not less than 0  

# # short-circuit evaluation
# # Short-circuit evaluation means that in an AND operation, if the first operand is False,
# # the second operand is not evaluated because the result will be False anyway.
# # In an OR operation, if the first operand is True, the second operand is not evaluated
# # because the result will be True anyway.
# print(False and (1 / 0))  # Output False, second operand is not evaluated
# print(True or (1 / 0))  # Output True, second operand is not evaluated 
# # Example of short-circuit evaluation
# x = 5
# y = 10
# print(x > 0 and y > 0)  # Output True, both conditions are True
# print(x > 0 or y < 0)  # Output True, at least one condition is True
# print(not (x < 0))  # Output True, x is not less than 0

# Definition for sequence 
# str = "Hello, World!"  # String sequence
# prefix = "Hello"  # Prefix for the string
# suffix = "World!"  # Suffix for the string
# substring = "lo, W"  # Substring to check in the string   
# sub-sequence = "lo, Wd"  # Subsequence to check in the string

# in operator
# name = "John Doe"
# print("John" in name)  # Output True, "John" is a substring of "John Doe"
# print("Jane" in name)  # Output False, "Jane" is not a substring of "John Doe"
# print("John" not in name)  # Output False, "John" is a substring
# print("Jane" not in name)  # Output True, "Jane" is not a substring 

# # not in operator
# print("John" not in name)  # Output False, "John" is a substring
# print("Jane" not in name)  # Output True, "Jane" is not a

# # modulus %2 and %10
# print(10 % 2)  # Output 0, 10 is even
# print(10 % 10)  # Output 0, 10 is divisible by
# print(12345 % 10)  # Output 5, last digit of 12345 is 5
# print(12345 % 100)  # Output 45, last two digits of 12345 are 45
# print(12345 % 1000)  # Output 345, last three digits of 12345 are 345   

# num % 2 
# Check if a number is even or odd

# num % 10
# Check the last digit of a number

# num // 100 
# Check the first two digits of a number

# Division and Modulus Homework 1

# Homework 1: Averags

# num1, num2, num3, num4, num5 = map(int, input("Enter five numbers separated by spaces: ").split())
# average = (num1 + num2 + num3 + num4 + num5) // 5
# print(average)  # Output the average of the five numbers

# sum_of_three_numbers = num1 + num2 + num3
# sum_of_two_numbers = num4 + num5

# sum_average = (sum_of_three_numbers / sum_of_two_numbers) 
# print(sum_average)  # Output the average of the sum of three numbers and the sum of two numbers

# avg_sum_of_three_numbers = (num1 + num2 + num3) / 3

# avg_sum_of_two_numbers = (num4 + num5) / 2

# sum_average_of_averages = (avg_sum_of_three_numbers/ avg_sum_of_two_numbers)
# print(sum_average_of_averages)  # Output the average of the averages

# # Homework 2: fractional part

# num_a , num_b = map(int, input("Enter two numbers separated by a space: ").split())
# fractional_part = (num_a / num_b) - (num_a // num_b)
# print(fractional_part)  # Output the fractional part of the division

# Homework 3: Remainder of Division
# n , m = map(int, input("Enter two numbers separated by a space: ").split())
# r = n // m  
# sum_remainder = n - m * r  # Calculate the remainder of the division
# print(sum_remainder)  # Output the remainder of the division  

# Division and Modulus Homework 2

# Homework 1: is even ?

# num = int(input("Enter a number: "))
# is_even1 = num % 2 == 0  # Check if the number is even
# print(is_even1)  # Output True if the number is even, False otherwise

# # is_even2 = 

# is_even3 = num % 10 
# last_digit = is_even3 == 0 or is_even3 == 2 or is_even3 == 4 or is_even3 == 6 or is_even3 == 8  # Check if the number is even using modulus
# print(last_digit)  # Output True if the last digit is even, False otherwise


# Homework 2: 
# sum = 0  # Initialize sum to 0

# num = int(input("Enter a number: "))
# sum1 = num % 10 
# num //= 10
# sum2 = num % 10
# num //= 10
# sum3 = num % 10
# num //= 10
# print(sum1 + sum2 + sum3)  # Output the sum of the last three digits

# homework 3: 4th digits from the end
# number = int(input("Enter a number: "))
# e = number % 10000
# e //= 1000
# print(e)

# Output the 4th digit from the end of the number
# Note: This code assumes that the number has at least 4 digits.
# If the number has less than 4 digits, it will output 0.
# You can add error handling to check for this condition if needed.
# Example: If the input is 12345678, the output will be 5.
# If the input is 1234, the output will be 0.

# Homework 3 : Division and Modulus

# Homework 1: 100 or 7?

# num = int(input("Enter a number: "))
# x = num % 2
# print(x and 7 or 100 )  # Output 7 if the number is odd, otherwise output 100

# Homework 2:Years!

# num = int(input("Enter a number: "))

# y = num / 360 
# m = (num % 360) / 30

# d =(num % 360) % 30

# print(f"Years: {int(y)}, Months: {int(m)}, Days: {int(d)}")  # Output the number of years, months, and days based on the input number

