'''
                          List Methods:
                      ---- Add method ----
Append() → appending and adding a elements to end of the list.
Extend() → adds the an
Insert → inserts a given index in a given index
                   ---- delete method ----
Remove() → removes the particular elements (note: in this elements should given)
Pop() → removes the particular elements (note : in this elements index value should given)
Clear → remove all the elements in a list.
            --- sort Method ------
Sort() → used to sort a list in ascending (or) descending order.

Reverse() → reverses the elements in a list.

Count() → counts the elements in a list

Min() → returns the minimum of all the elements in a list 
Max() → returns the maximum of all the elements in a list



Copy() → it returns the copy of the list.
Index → returns a index values of the elements
____________________________________________________________________________________________________________________________________________________
'''
# # List is a ordered, Chengeable and allow duplicates

# num=[1,5,7,5,8,1,8,1]
# print(num)      #1,5,7,5,8,1,8,1
#
# print(num[5])   #1
# print(num[0:3]) #1,5,7
# print(num[:-3]) #1,5,7,5,8
# print(num[-3:]) #1,8,1
# print(len(num)) #8
#
# # add method _____________________________________________________________________________________________________________________________
# num=[1,5,7,5,8,1,8,1]
#
# num.append(4)
# print(num)                  # 1, 5, 7, 5, 8, 1, 8, 1, 4
#
#
# num.insert(0,9)
# print(num)                  # 9, 1, 5, 7, 5, 8, 1, 8, 1, 4
#
#
# num.extend([10,6,52,47])
# print(num)                  # 9, 1, 5, 7, 5, 8, 1, 8, 1, 4, 10, 6, 52, 47
#
#
# num[1:3]=48,53,52
# print(num)                  # 9, 48, 53, 52, 7, 5, 8, 1, 8, 1, 4, 10, 6, 52, 47
#
# # delete method _________________________________________________________________________________________________________________________
# num=[1,2,3,4,5]
#
# num.pop(1)
# print(num) # 1,3,4,5
#
# del num[2]
# print(num) # 1,3,5
#
# # This sort method _______________________________________________________________________________________________________________________
# num = [1,8,2,7,45,7]
# num.sort()
# print(num)  # 1,2,7,7,8,45
#
# # Reverse _________________________________________________________________________________________________________________________________________________________________
# num = [1,25,28,25,10]
# for i in reversed(num):
#     print(i,end=" ")   # 10 25 28 25 1
#
# num.reverse()
# print(num)           # 10, 25, 28, 25, 1
#
# num.sort(reverse=True)
# print(num)              # 28, 25, 25, 10, 1
#
# num.sort(reverse=False)   # The is a not reverse method
# print(num)                # 1, 10, 25, 25, 28
#
# # Count _______________________________________________________________________________________________________________________________________________
# num =[1,5,8,9,7,6,2,3,4,10]
# num.sort()
# num.count(num)
# print(num)
#
# # min max ____________________________________________________________________________________________________________________________________________________________
# num =[1,2,58,258,69,24,8,2,96,30]
# x=min(num)
# y=max(num)
# print(x)  # 1
# print(y)  # 258
#
# print(min(num))  # 1
# print(max(num))  # 258
#
# # Copy ___________________________________________________________________________________________________________________________________________________________________________
# num = [1,25,7,8,5,9,4,1]
# copy=num
# return .copy
# x=()
# x=copy
# print(x)

