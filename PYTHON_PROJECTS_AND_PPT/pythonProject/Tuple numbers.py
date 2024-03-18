'''
                          Tuple Methods:

* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Unchangeable :Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
* Index : Tuple items are indexed, the first item has index [0], the second item has index [1] etc
* Tuple Length : To determine how many items a tuple has, use the len() function:
* Data Types  : Tuple items can be of any data type:
* count()	Returns the number of times a specified value occurs in a tuple
* index()	Searches the tuple for a specified value and returns the position of where it was found

* type()  : From Python's perspective, tuples are defined as objects with the data type 'tuple':

* Negative Indexing : Negative indexing means start from the end. (-1 refers to the last item, -2 refers to the second last item etc.)

* Change Tuple Values : Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

* Unpacking a Tuple : When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
* packing a Tuple   : But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
*Using Asterisk* : If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
 '''

'''
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
'''
# #How to sort a Tuple in Python?
# x= (11,88,42,8,10,70,12,77,11)
# x=list(x)
# x.sort()
# print(x)
# x=tuple(x)
# print(x)
#
# # How remove elements in a Tuple?
# x=(1,25,5,8,6,7,9)
# x=list(x)
# x.remove(1)
# x=tuple(x)
# print(x)
#
# # How to append
# x=(1,25,5,8,6,7,9)
# x=list(x)
# x.append(1)
# x=tuple(x)
# print(x)
#
# # print tuple , acceessing, replacing an element from tuple
# x = (1,5,8,8,9)
# x=list(x)
# x[2]=7
# x=tuple(x)
# print(x)
#
# # How to merge multiple Tuples in Python?
# tuple1 = (1,25,5,9)
# tuple2 = (2,8,8,68)
# tuple3 = (3,58,5,812)
# marge_multiple = tuple1 + tuple3 +tuple2
# print(marge_multiple)
#
# # create a nested Tuple and access its elements
# nested_tuple =( (1,2,3,5,4) , ("suresh","giri","suresh"), (True,False))
# element_1_2 = nested_tuple[0][1]
# element_2_3 = nested_tuple[1][2]
# element_3_1 = nested_tuple[2][0]
# print("Element at index [0][1]:", element_1_2)
# print("Element at index [1][2]:", element_2_3)
# print("Element at index [2][0]:", element_3_1)
#
# # adding 6 how to
# Tuple = (1,2,3,4,5)
# Tuple = list(Tuple)
# Tuple.append(6)
# Tuple = tuple(Tuple)
# print(type(Tuple))
# print(Tuple)
#
# # how to (1,2,3,4,5[7,8,9])
# t = (1,2,3,4,5,[7,8,9])
# print(t[5][0])
# t[5][0]=25
# print(t)
# print(type(t))
#
# # #__________________________________________________________________________________________________________________________________________________________________________________________________________
# t = (1,2,3,4,5,6)
# t1 = (7,8,9,10,11,12)
#
# print('x' in t)
# print('x' in t1)
# print('x' not in t)
# print('x' not in t1)
#
# print(t[2:6])
# print(t1[0:5])
#
# print(t[0:5:2])
# print(t1[0:6:2])
#
# print(t[:-3])
# print(t1[:-4])
#
# print(t+t1)
# print(t1+t)



