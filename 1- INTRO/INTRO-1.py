# # This is a simple Python script to print a greeting message
# # printing
# print('hello mohamed')
# print("hello mohamed")

# """This is a multi-line comment
# It can span multiple lines
# and is often used to explain complex logic or provide documentation."""

# #  \n --> The following line prints a message to the console

# print("hello mohamed \nhow are you?")
# #  \t --> The following line prints a message with a tab space
# print("hello mohamed \t how are you?")

# # , --> The following line prints multiple items separated by a space
# print("hello", "mohamed", "how are you?")

# # \'# The following line prints a message with a single quote
# print('hello mohamed\'s world')

# # \" --> The following line prints a message with a double quote
# print("hello mohamed\"s world")

# # Homework: PRINTING

# # HOMEWORK: 1#: Guess the run-time output
# print('Practice' , "Makes Perfect.")
# print("Children must be taught\n how to think\n not\n what to think.")
# print("\"\"")
# print('2 * 3 * 4 * 5 / 10 = ')
# print(2 * 3 * 4 * 5 / 10)

# # HOMEWORK: 2#: 
# print('Print(\"Me\")')
# print("Print('Me')")
# print('Print(\'Me\")')
# print('you will learn \n alot')

# # HOMEWORK: 3#:Write code to print the following
# print("*")
# print("**")
# print("***")
# print("****")
# # HOMEWORK: 4#: Write code to print the following
# print("     *     ")
# print("    ***    ")
# print("   *****   ")
# print("  *******  ")
# print(" ********* ")    

# # HOMEWORK: 5#: Write code to print the following
# print("     *     ")
# print("    ***    ")
# print("   *****   ")
# print("  *******  ")
# print(" ********* ")
# print("  *******")
# print("   *****  ")
# print("    ***   ")
# print("     *     ")
# # HOMEWORK: 6#: Write code to print the following
# print('Hi')
# print('')
# print('I am Mohamed')
# print(3 * 5)
# print("woderful day")
# print("wonderful day")

# # Data Types AND Variables
# # Data types are the classification of data items. In Python, data types are used to define
# # the type of a variable, which determines what kind of operations can be performed on it.
# # Variables are used to store data values. In Python, variables do not need to be declared with a specific type.
# # Python has several built-in data types, including:
# # 1. Numeric Types: int, float, complex
# # 2. Sequence Types: list, tuple, range
# # 3. Text Type: str
# # 4. Mapping Type: dict
# # 5. Set Types: set, frozenset
# # 6. Boolean Type: bool
# # 7. Binary Types: bytes, bytearray, memoryview
# # Variables are created when you assign a value to them. For example:


# var = 55 
# var = 10 
# print(var)  # This will print the value of var, which is 10
# print(type(var))  # This will print the type of var, which is <class 'int'>
# var = var + 5  # This will add 5 to the current value of var
# print(var)  # This will print the new value of var, which is 15 
# print(type(var))  # This will still print the type of var, which is <class 'int'>
# var = 6.5 # This will assign a float value to var
# print(var)  # This will print the value of var, which is 6.5
# print(type(var))  # This will print the type of var, which is <class 'float'>
# var = 3 * var - var 
# print(var)  # This will print the value of var, which is 6.5 (3 * 6.5 - 6.5 = 13 - 6.5 = 6.5)   
# print(type(var))  # This will still print the type of var, which is <class 'float'>
# var = 'eng.mohamed' # This will assign a string value to var
# print(var)  # This will print the value of var, which is 'eng.mohamed'
# print(type(var))  # This will print the type of var, which is <class 'str'>

# print('Hello, World!')  # This will print a string to the console
# print('I am '+ ' ' + 'Mohamed')  # This will concatenate strings and print 'I am Mohamed    
# print('I am ' + str(3 * 5))  # This will concatenate a string with the result of an arithmetic operation
# str1 = 'I am '
# str2 = 'Mohamed'
# print(str1 + str2)  # This will concatenate str1 and str2 and print

# print(str1 * 3)  # This will repeat str1 three times and print 'I am I am I am '
# print(str2 * 3)  # This will repeat str2 three times and print '

# print(2 * str1 + str2)  # This will repeat str1 two times and print 'I am I am '/   

# print("""Hello, World!""")  # This will print a multi-line string

# print('''Hello, World!''')  # This will also print a multi-line string

# min_val = min(1, 2) # This will find the minimum value in the list
# print(min_val)  # This will print the minimum value, which is 1
# max_val = max(1, 2) # This will find the maximum value in the list
# print(max_val)  # This will print the maximum value, which is 2

# str_val = 'Hello, World!'  # This will assign a string value to str_val
# print(len(str_val))  # This will print the length of the string, which is 13


# #  conversion between data types

# int_val = 10  # This will assign an integer value to int_val
# float_val = float(int_val)  # This will convert int_val to a float
# print(float_val)  # This will print the float value, which is 10.0
# str_val = str(int_val)  # This will convert int_val to a string
# print(str_val)  # This will print the string value, which is '10'
# bool_val = bool(int_val)  # This will convert int_val to a boolean
# print(bool_val)  # This will print the boolean value, which is True (since int
# # is non-zero)


# # reading input from the user
# user_input = input("Enter your name: ")  # This will prompt the user to enter their name
# print("Hello, " + user_input + "!")  # This will print a greeting message with the user's 

# a,b,c = input("Enter three numbers separated by spaces: ").split()  # This will prompt the user to enter three numbers
# a = int(a)  # This will convert the first number to an integer
# b = int(b)  # This will convert the second number to an integer
# c = int(c)  # This will convert the third number to an integer
# print("The sum of the three numbers is: ", a + b + c)  # This will print the sum of the three numbers

# a,b,c = map(int,input("Enter three numbers separated by spaces: ").split())  # This will prompt the user to enter three numbers and convert them to integers
# print("The sum of the three numbers is: ", a + b + c)  #


# # 08 variables homework 1 - 4 easy challenges

# # homework 1: math operations
# num1 = input("Enter the first number: ") 
# num2 = input("Enter the second number: ")

# num1_float = float(num1)    
# num2_float = float(num2)  
# # This will convert the input strings to float numbers
# print(num1 + '+' + num2, '=', num1_float + num2_float)  # This will print the sum of the two numbers
# print(num1 + '-' + num2, num1_float - num2_float)  # This will print the difference of the two numbers
# print(num1 + '*' + num2, '=', num1_float * num2_float)  # This will print the product of the two numbers
# print(num1 + '/' + num2, '=', num1_float / num2_float)  # This will print the quotient


# # homework 2: Student grades 

# student_name = input("Enter the student's name: ")  # This will prompt the user to enter the student's name
# student_id = input("Enter the student's ID: ")  # This will prompt the user to enter the student's ID
# student_grade = float(input("Enter the student's grade: "))  # This will prompt the user to enter the student's grade

# student_name2 = input("Enter the second student's name: ")  # This will prompt the user to enter the second student's name
# student_id2 = input("Enter the second student's ID: ")  # This will prompt the user to enter the second student's ID
# student_grade2 = float(input("Enter the second student's grade: "))  # This will prompt the user to enter the second student's grade

# print( 'Information for students and thier "math" grades:')
# print(student_name + " (ID" + student_id + ") got grade:" , student_grade) # This will print the first student's information
# print(student_name2 + " (ID" + student_id2 + ") got grade:", student_grade2)  # This will print the second student's information

# average_grade = (student_grade + student_grade2) / 2  # This will calculate the average grade of the two students
# print("Avarage math grade ", average_grade)  # This will print the average grade


# # homework 3: Even and odd sum

# num1 , num2, num3 , num4 , num5 , num6 , num7 , num8 = map(int,input("Enter eight numbers separated by spaces: ").split())  # This will prompt the user to enter eight numbers and convert them to integers

# even_sum = num2 + num4 + num6 + num8  # This will calculate the sum of the even numbers
# odd_sum = num1 + num3 + num5 + num7  # This will calculate

# # the sum of the odd numbers
# print("The sum of the even numbers is: ", even_sum)  # This will print the sum of the even numbers
# print("The sum of the odd numbers is: ", odd_sum)  # This will print the sum of the odd numbers


# homework 4: Special concatenation

# str1 , str2, str3 = input("Enter three strings separated by spaces: ").split()  # This will prompt the user to enter three strings
# str_concat = str1 +"'"+str2+'"'+str3  # This will concatenate the three strings with special characters
# print("The concatenated string is: ", 10 * str_concat)  # This will print the concatenated string repeated 10 times 

# 09 variables homework 2 - 2 medium challenges

# homework 1: Guess Output

# num1 = 1
# num2 = 2

# num3 = num1 + num2  # This will calculate the sum of num1 and num2
# num1 = num2 # This will assign the value of num2 to num1
# num2 = num3  # This will assign the value of num3 to num2

# num3 = num1 + num2  # This will calculate the new sum of num1 and num2
# num1 = num2  # This will assign the value of num2 to num1
# num2 = num3  # This will assign the value of num3 to num2

# num3 = num1 + num2  # This will calculate the new sum of num1 and num2
# num1 = num2  # This will assign the value of num2 to num1
# num2 = num3  # This will assign the value of num3 to num2

# num3 = num1 + num2  # This will calculate the new sum of num1 and num2
# num1 = num2  # This will assign the value of num2 to num1
# num2 = num3  # This will assign the value of num3 to num2

# num3 = num1 + num2  # This will calculate the new sum of num1 and num2
# num1 = num2  # This will assign the value of num2 to num1
# num2 = num3  # This will assign the value of num3 to num2

# num3 = num1 + num2  # This will calculate the new sum of num1 and num2
# num1 = num2  # This will assign the value of num2 to num1
# num2 = num3  # This will assign the value of num3 to num2

# print("num3 =", num3)  # This will print the final value of num3


# homework 2: Swapping 2 numbers!

# num1 , num2 = map(int, input("Enter two numbers separated by a space: ").split())  # This will prompt the user to enter two numbers and convert them to integers

# num3 = num1  
# num1 = num2 
# num2 = num3

# print(num1 , num2)


# 10 variables homework 3 - 3 hard challenges

# homework 1 : swapping 3 numbers!

# num1 , num2 , num3 = map(int,input('Enter three numbers: ').split())
# num1 , num2 , num3 = num2 , num3 , num1 
# print(num1,num2 ,num3)

# num1 , num2 , num3 = map(int,input('Enter three numbers: ').split())

# temp = num1 
# num1 = num2 
# num2 = num3 
# num3 = temp

# print(num1,num2 ,num3)


# homework 2: Print Me

# A , B = map(float,input('Enter two numbers: ').split())

# sum = ( B + 0 ) * A * A + 1   
# print('The result is:', sum)

n = int(input('Enter number: '))

sum = n * (n+1 / 2)
print(sum)