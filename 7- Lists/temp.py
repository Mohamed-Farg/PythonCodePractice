def f1(lst):
    lst[0]=10

def f2(lst):
    lst = [7,8,9]
    return lst

my_lst = [1,2,3,4,5]

another_lst = my_lst
print(another_lst is my_lst )

f1(another_lst)
print(my_lst[0])


f1(my_lst)
print(my_lst[1])

my_lst = f2(my_lst)
print(my_lst[1])
print(another_lst[1])