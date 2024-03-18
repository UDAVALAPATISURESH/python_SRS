'''
                                        Set
* Sets are used to store multiple items in a single variable.
* Set is one of 4 built-in data types in Python used to store collections of data, the
other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
* A set is a collection which is unordered, unchangeable*, and unindexed.

                         Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

                         Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

                       Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.

                    Duplicates Not Allowed
Sets cannot have two items with the same value.

Change Items
Once a set is created, you cannot change its items, but you can add new items.
'''

'''
Duplicates Not Allowed
'''
'''
Loop through the set, and print the values:

                Add Items
Add an item to a set, using the add() method

                Add Sets
To add items from another set into the current set, use the update() method

            Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

                        Remove Item
* To remove an item in a set, use the remove(), or the discard() method.
* Remove "banana" by using the discard() method:
* Remove a random item by using the pop() method:
* The clear() method empties the set:
* The del keyword will delete the set completely:

              Loop Items
You can loop through the set items by using a for loop:

             Join Two Sets
The union() method returns a new set with all items from both sets:
The update() method inserts the items in set2 into set1:

               Keep ONLY the Duplicates
The intersection_update() method will keep only the items that are present in both sets.
The intersection() method will return a new set, that only contains the items that are present in both sets.

              Keep All, But NOT the Duplicates
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

Method                                 Description

add()                                 Adds an element to the set
clear()	                              Removes all the elements from the set
copy()	                              Returns a copy of the set
difference()	                      Returns a set containing the difference between two or more sets
difference_update()	                  Removes the items in this set that are also included in another, specified set
discard()	                          Remove the specified item
intersection()	                      Returns a set, that is the intersection of two other sets
intersection_update()	              Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                      Returns whether two sets have a intersection or not
issubset()	                          Returns whether another set contains this set or not
issuperset()	                      Returns whether this set contains another set or not
pop()	                              Removes an element from the set
remove()	                          Removes the specified element
symmetric_difference()	              Returns a set with the symmetric differences of two sets
symmetric_difference_update()	      inserts the symmetric differences from this set and another
union()	                              Return a set containing the union of sets
update()	                          Update the set with the union of this set and others
'''
# find adress stor
# import sys
# set1 = {"suresh","hari","kumar","giri"}
# set2 = {"suresh","hari","kumar","giri"}
# set3 = {"suresh","hari","kumar","giri"}
# set4 = {"suresh","hari","kumar","giri"}
#
# print("Size of Set3:" + str (sys.getsizeof(set1)) + "bytes")
# print("Size of Set3:" + str (sys.getsizeof(set2)) + "bytes")
# print("Size of Set3:" + str (sys.getsizeof(set3)) + "bytes")
# print("Size of Set3:" + str (sys.getsizeof(set4)) + "bytes")
#
# print(sys.getsizeof(set1))
# print(sys.getsizeof(set2))
# print(sys.getsizeof(set3))
# print(sys.getsizeof(set4))
#
# print(type(set1))
# print(type(set2))
# print(type(set3))
# print(type(set4))
# print(set1)
# print(set2)
# print(set3)
# print(set4)
# set1.add("ravi")
# print(set1)
# add method

# # add() ______________________________________________________________________________________________________________________________________________________
# num = {1,2,3,4,5,6,7,8}
# num.add(9)
# print(num)

# # update()______________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,5,1,5,}
# num.update({4})
# print(num)

# # union()______________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,2,4,5,6}
# num1 = {7,8,9,10}
# num=num1.union(num)
# print(num)

# # difference()___________________________________________________________________________________________________________________________________________________________________________
# num = {1,2,2,3,5,4,7,6}
# num1 = {1,2,3,5,8}
# num2 = num.difference(num1)
# print(num2)
#
# num = {1,2,2,3,5,4,7,6}
# num1 = {1,2,3,5,8}
# num3 = num1.difference(num)
# print(num3)

# # difference_update()________________________________________________________________________________________________________________________________________________________________________
# num ={1,2,3,4,5,6}
# num1 ={5,6,7,8,9,10,11}
# num.difference_update(num1)
# print(num)


# num ={1,2,3,4,5,6}
# num1 ={5,6,7,8,9,10,11}
# num1.difference_update(num)
# print(num1)

# # symmetric_difference()________________________________________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,4,5,6}
# num1 = {4,5,6,7,8,9,10,11,12}
# num=num.symmetric_difference(num1)
# print(num)


# num = {1,2,3,4,5,6}
# num1 = {4,5,6,7,8,9,10}
# num1 = num1.symmetric_difference(num)
# print(num1)

# # symmetric_difference_update()__________________________________________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,4,5,6}
# num1 = {4,5,6,7,8,9,10}
# num.symmetric_difference_update(num1)
# print(num)

# num = {1,2,3,4,5,6}
# num1 = {4,5,6,7,8,9,10}
# num1.symmetric_difference_update(num)
# print(num1)

# # copy()_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,4,5}
# num1 = num.copy()
# print(num1)

# # remove()____________________________________________________________________________________________________________________________________________________________________________________________________
# # discard()________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# # pop()_____________________________________________________________________________________________________________________________________________________________________________________________________
# # clear()________________________________________________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,4,5,7,8,9,10}
# print(num)
# num.remove(1)
# print(num)
#
# num.discard(2)
# print(num)
#
# num.pop()
# print(num)
#
# num.clear()
# print(num)
# #Emty
# print(num)

# # intersection()_____________________________________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,4,5}
# num1 = {5,6,7,8,9,10}
# num3 = num.intersection(num1)
# print(num3)

# # intersection_update()______________________________________________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,4,5}
# num1 = {3,4,5,6,7,8,9,10}
# num.intersection_update(num1)
# print(num)

# # isdisjoint() _______________________________________________________________________________________________________________________________________________________________________
# False
# num = {1,2,3,4,5}
# num1 = {3,4,5,6,7,8,9,10}
# num2 = num.isdisjoint(num1)
# print(num2)
# # True
# num = {1,2,3,4,5}
# num1 = {6,7,8,9,10}
# num2 = num.isdisjoint(num1)
# print(num2)

# # issubset()____________________________________________________________________________________________________________________________________________________________________________________________________
# False
# num = {1,2,3,4,5}
# num1 = {4,5,6,7,8,9,10}
# num3 = num.issubset(num1)
# print(num3)

# True

# num = {1,2,3,4,5}
# num1 = {6,7,8,9,10,1,2,3,4,5}
# num3 = num.issubset(num1)
# print(num3)

# # issuperset()_____________________________________________________________________________________________________________________________________________________________________________________________________________________________
# num = {1,2,3,4,5}
# num1 = {6,7,8,9,10,1,2,3,4,5}
# num3 = num.issubset(num1)
# print(num3)

# num = {1,2,3,4,5,7,9,5}
# print(max(num))
# print(min(num))
# print(sum(num))
# print(len(num))































