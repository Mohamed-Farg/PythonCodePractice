# Mutable Objects

# id() function

# name = ' mostafa'
# another = name 

# the same memory address : name and another 
# print(id(name))
# print(id(another))

# x = 10 
# print(id(x))

# with objects

# class Employee:
#     def __init__(self,name):
#          self.name = name

# obj1 = Employee('mohamed') 
# print(id(obj1))


# class Employee:
#     def __init__(self,name):
#          self.name = name


# # the same memory address : obj1 and obj2 
# obj1 = Employee('mohamed') 
# print(id(obj1))

# obj2 = obj1
# print(id(obj2))


# class Employee:
#     def __init__(self,name):
#          self.name = name


# # the same memory address : obj1 and obj2 
# obj1 = Employee('mohamed') 
# print(id(obj1))

# obj2 = obj1
# print(id(obj2))

# # not the same memory adderss because it creating new object 
# obj3 = Employee("ahmed")
# print(id(obj3))

# class Employee:
#     def __init__(self):
#         self.id = 0

# def inc_id(emp):
#     print(id(emp))
#     emp.id += 1

# obj1 = Employee()
# obj2 = obj1

# print(id(obj1))
# print(id(obj2))

# print(obj1.id)

# inc_id(obj1)
# print(obj1.id)

# inc_id(obj2)
# print(obj1.id)
# print(obj2.id)

# Python has built-in mutable classes:
#  list, dict, set, bytearray

# Immutable objects
# int, float, bool, complex, tuple, frozenset, unicode

# Memory for immutable objects

# x = 30 
# y = x 
# z = 30 

# print(id(x))
# print(id(y))
# print(id(z))
# print(id(30))


# x += 10 
# print(id(x))
# print(id(y))

# x = 30 
# print(id(x))

# Same concepts with other immutable objects with string 

# x = 'Hey'
# y = x 
# z = 'Hey'

# print( x is z)

# print(id(x))
# print(id(y))
# print(id(z))
# print(id('Hey'))

# x += 'most'
# print(id(x))
# print(id(y))

# x = 'Hey'
# print(id(x))

# Tuple: mix of mutable and immutable

# class Employee:
#     def __init__(self,name):
#         self.name = name
# # mutable
# obj1 = Employee('mohamed')
# # immutable
# obj2 = 'ahmed'

# my_tuple = (obj1,obj2)

# y , z = my_tuple
# print(y.name)


# obj1.name = 'mido'

# y , z = my_tuple
# print(y.name)


# Identity Operator

# is : return ture if two variables are the same object (memory)

# str1 = 'mohamed'
# str2 = str1
# str3 = str2

# print(id(str1),id(str2),id(str3))

# print(str1 is str3)

# class Employee:
#     def __init__(self,name):
#         self.name = name

# obj1 = Employee('mohamed')
# obj2 = Employee('ahmed')
# obj3 = obj2

# print(id(obj1),id(obj2),id(obj3))
# print(obj2 is obj1)
# print(obj2 is obj3)
# print(obj2 is not obj3)

# Is for checking types

# x = 1 
# if type(x) is int:
#     print('an int')

# y = None

# print(y is None)
# print(x is not None)

# print(type(2.5) is float)

# class Employee:
#     def __init__(self,name):
#         self.name = name

# obj1 = Employee('mohamed')
# print(type(obj1) is Employee)
        

# Mutable objects!
# true
# x , y = 30 , 15 + 15
# print( x is y)
# # false 
# x , y = x * 10000 , y * 10000
# print( x is y)
# # true
# x , y = 'hello' , 'hello'
# print( x is y)
# # false 
# x , y = x * 1000 , y * 1000
# print( x is y)
# true
# x , y = 'hello!' , 'hello!'
# print( x is y)
# # true
# z = x 
# print( x is z )

# Is vs ==

# is : check if same memory/reference 
# == : check if equal value!

# x , y = 123456789 , 123456789

# print( x == y ) 
# print( x is y )

# x , y = 10 , 10 
# print(x is y)

# Garbage Collector (CPython)

# def f2(tt):

#     print(tt)


# def f1():
#     s1 = 'Hey'
#     s2 = s1 
#     f2(s2)
#     del s2 

# f1()

# List Data Structure

# Creating a list

# my_list = [1,2,3,4]
# print(len(my_list))

# print(2 in my_list)
# print(9 in my_list)
# print()

# for item in my_list:
#     print(item)
# print()

# print(my_list)

# my_list = [1, 'mohamed', 4.5]
# print(my_list)


# indexing

# numbers = [10,2,7,5,3]
# numbers[0] = 9
# numbers[2] *= 3
# numbers[4] += 1 
# print(numbers[4])

# for i in range(5):
#     print(numbers[i],end=' ')
# print()

# + and * operators 
# my_list = [1,'mohamed',4]
# another_list = [99,11.5]

# coc_list = my_list + another_list
# print(coc_list)
# thrd_lst = 2 * another_list
# print(thrd_lst)
# lst = [0] * 6 
# lst += [2,3] +[5]
# print(lst)


# List Methods

# Append, extend and insert

# my_list = [1,5,10,17,2]

# my_list.append('Hii')
# print(my_list)

# another_lst = [3,1]
# my_list.extend(another_lst)
# print(my_list)

# my_list.insert(2,'Wow')
# print(my_list)

# for i in my_list:
#     print(i,end= ' ')
# print()

# Pop, remove + del statement
# my_list = [1, 5, 10, 17, 2, 'Hii']

# print(my_list.pop())
# print(my_list.pop(3))

# del my_list[0]
# print(my_list)
# my_list.remove(10)
# print(my_list)

# Index and clear methods

# my_list = [ 1,15,7,'mohamed',7,True,0]

# print(my_list.index(7))
# print(my_list.index('mohamed'))
# print(my_list.index(True))
# print(my_list.index(False))

# my_list.clear()
# print(len(my_list))

# Count method

# my_list = [4,5,7,4,5,4,8]
# print(min(my_list),max(my_list))

# print(my_list.count(4))
# print(my_list.count([4,5]))

# my_list = ['ali','ALI','ali']
# print(my_list.count('ali'))

# + vs +=

# += is changing in-place

# lst = [1,2,3]
# print(id(lst))

# lst += [4]
# print(id(lst))

# lst = lst + [5]
# print(id(lst))

# lst += ['Hey']
# print(lst)

# lst += 'Hey'
# print(lst)

# Sorting and Reversing Methods

# Sort Method
# lst = [5,7,2]
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = lst.sort()
# print(lst)

# Sorted function

# lst = [5,7,2]
# lst_sorted_cpy = sorted(lst)
# print(lst_sorted_cpy)

# my_str = 'zacb'

# new_str = sorted(my_str)
# print(new_str)

# new_str = sorted(my_str,reverse=True)
# print(new_str)

# Reverse Method .... Reversed Function

# my_list = [1,2,3,4]

# my_list.reverse()
# print(my_list)

# my_list += ['Hi']
# print(my_list)

# new_lst = reversed(my_list)
# new_lst_rev  = list(reversed(my_list))
# print(new_lst_rev)


# new_lst_rev2 = my_list.copy()
# new_lst_rev2.reverse()
# print(new_lst_rev2)

# Iterate in a reversed order

# lst = [7,8,9,'Hi']

# for pos in range(len(lst)):
#     print(lst[len(lst) - pos - 1],end = ' ')
# print( )

# # Python 
# for idx in range(len(lst) - 1 , -1 ,-1 ):
#     print(lst[idx],end = ' ')
# print()

# # Better 
# for i in reversed(lst):
#     print(i,end =' ')
# print()


# # creating copy from list 
# for pos , item in reversed(list(enumerate(lst))):
#     print(pos,item,nd='-')


# List with Functions

# Flexible Reading


# my_list = input().split()

# for item in my_list:
#     print(item, end=' ')
# print()

# now list of int 
# my_list = list(map(int,input().split()))

# print(type(my_list),type(my_list[0]))

# for item in my_list :
#     print(item,end= ' ')
# print()

# sum, min, max, help functions

# my_list = [4,5,7,4,5,4,8]
# print(sum(my_list))

# print(min(my_list),max(my_list))

# my_list = ['ali','zaid','mostafa']

# print(min(my_list),max(my_list))

# help(my_list.count)

# enumerate function

# my_list = [1,'mostafa',4]
# for idx , item in enumerate(my_list):
#     print(idx,item)
#     idx = -100

# lst = list(enumerate(range(5,9)))

# for item in lst:
#     print(item)

# all and functions

# lst = [ 10,20,-12,'mostafa']

# print(all(lst))
# print(all([]))

# print(all([False]))
# print(all(['']))
# print(all([0]))

# print(all([10,0,2]))

# lst = [10,20,0,'mostafa']

# print(all(lst))
# print(any(lst))

# Mutability

# def f1(lst):
#     lst[0] = 10 

# def f2(lst):
#     lst = [7,8,9]
#     return lst

# my_lst = [1,2,3,4,5]

# another_lst = my_lst
# print(another_lst is my_lst)

# # another_lst  = [1,2,3,4,5]
# # f1(another_lst)
# # another_lst  = [10,2,3,4,5]
# # print(my_lst[0])
# # for i in another_lst:
# #     print(i, end = ' ')

# f2(my_lst)
# print(my_lst[1])
# for i in my_lst:
#     print(i, end = ' ')
# print()
# my_lst = f2(my_lst)
# print(my_lst[1])
# print(another_lst[1])

# Copy and is

# lst = list('mostafa')
# print(len(lst))
# print(lst)

# lst1 = lst 
# print(lst is lst1)

# new_lst = lst.copy()
# print(lst is new_lst)

# print(new_lst is new_lst + [1])


# Comparison

# lst1 = [1,5,8]
# lst2 = [1,5,8]
# lst3 = [1,5]
# lst4 = [7,5]

# print(lst1 is lst2)
# print(lst1 == lst2)

# print([1,2,3] is [1,2] + [3])
# print([1,2,3] == [1,2] + [3])

# print(lst1 < lst2)
# print(lst1 <= lst2)
# print(lst1 <= lst3)
# print(lst1 <= lst4)


# def our_reverse(lst):
#    for pos1 in range(len(lst)//2):
#      pos2 = len(lst) - pos1 - 1
#      lst[pos1],lst[pos2] = lst[pos2],lst[pos1]
      

# def main():
#     lst = list(map(int,input().split()))
#     our_reverse(lst)
#     print(lst)


# main()

# print(__name__)
# def our_reverse(lst):
   
#    if len(lst) <= 1:
#       return 
   
#    for pos1 in range(len(lst)//2):
#      pos2 = len(lst) - pos1 - 1
#      lst[pos1],lst[pos2] = lst[pos2],lst[pos1]
      

# if __name__ =='__main__':
#     lst = list(map(int,input().split()))
#     our_reverse(lst)
#     print(lst)


# Practice: Find pair values of maximum sum

# def max_sum(lst):
#    pos1 ,pos2 = 0,1
#    for i in range(len(lst)): 
#       for j in range(i + 1, len(lst)):
#         if lst[pos1] + lst[pos2] < lst[i] + lst[j]:
#            pos1,pos2 = i ,j
#    return pos1,pos2
      
# if __name__ =='__main__':
#     lst = list(map(int,input().split()))
#     pos1 , pos2 = max_sum(lst)
#     print(pos1 ,"value",lst[pos1]," ,,,,, ",  pos2 ,"value",lst[pos2])

# Find the index of maximum value in a list

# solution 1

# def get_max(lst):
    
#    if len(lst) < 2:
#         return None , None
    
#    first , second = float("-inf"),float("-inf")
    
#    for idx ,value in enumerate(lst):
#       if first < value :
#             second = first 
#             first = value 
#       elif second < value:
#             second = value

#    return first , second

# lst = [1,32,423,12,434]
# print(get_max(lst))


# solution 2

# def argMax(lst):
    
#     if len(lst) == 0 :
#         return None
#     return lst.index(max(lst))

# def top2_argMax(lst):
    
#     if len(lst) < 2:
#         return None , None
    
#     max_pos = argMax(lst)
#     max_val = lst[max_pos]

#     mn_value = min(lst)
#     lst[max_pos] = mn_value - 1

#     max2_pos = argMax(lst)

#     lst[max_pos] = max_val

#     return max_pos , max2_pos 


# lst = [10,20,3,30,7]
# print(top2_argMax(lst))

# solution 3

# def top2_argmaxV2(lst):
#     if len(lst) < 2:
#         return None , None
    
#     max1_pos , max2_pos = 0,1

#     if lst[max1_pos] < lst[max2_pos]:
#         max1_pos ,max2_pos= 1, 0
      
#     for cur_pos in range(2, len(lst)):
#       if lst[max1_pos] < lst[cur_pos]:
#           max1_pos,max2_pos = cur_pos, max1_pos
#       elif lst[max2_pos] < lst[cur_pos]:
#           max2_pos = cur_pos
      
#     return max1_pos , max2_pos 
    
# lst = [10,20,3,30,7]
# print(top2_argmaxV2(lst))



# Practice: Find most frequent number

# def most_freq_slow(lst):
#     most_value ,freq = None ,0 
#     for value in lst:
#         cnt = lst.count(value)
#         if cnt > freq:
#             most_value ,freq = value ,cnt 
#         elif cnt == freq :
#             most_value = min(most_value ,value)
#     return most_value ,freq 


# if __name__ == '__main__':
#     lst = list(map(int,input().split()))
#     most_value , freq = most_freq_slow(lst)

#     print('value', most_value , 'repeated' ,freq)


# def most_freq_fast(lst):
    
#     freq_lst = [0] * (max(lst) + 1)

#     for value in lst:
#         freq_lst[value] += 1

#     most_value = freq_lst.index(max(freq_lst))

#     return most_value , freq_lst[most_value]
    
# if __name__ == '__main__':
#     lst = list(map(int,input().split()))
#     most_value , freq = most_freq_fast(lst)

#     print('value', most_value , 'repeated' ,freq)



# 10 Homeword 1 - 7 Easy to Medium Challenges

# Homework 1

# Homework 1: Is increasing array?

# def increacing_arr(lst):
#     for idx in range(1,len(lst)):
#         if lst[idx] < lst[idx - 1]:
#             return False
#     return True

# if __name__ == '__main__':
#     lst = list(map(int,input().split()))

#     if increacing_arr(lst):
#         print("YES")
#     else:
#         print("NO")

# Homework 2: Replace MinMax

def replace_min_max_inplace(lst):
    mn = min(lst)
    mx = max(lst)

    for item in range(len(lst)):
        if lst[item] == mn:
            lst[item] = mx
        elif lst[item] == mx:
            lst[item] = mn

if __name__ == '__main__':
    lst = list(map(int,input().split()))

    replace_min_max_inplace(lst)
    print(lst)