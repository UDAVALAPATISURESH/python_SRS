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
# # Add method _____________________________________________________________________________________________________________________________________________
# names = ["suresh","giri","murali","ravi","nani","somu"]
# names.append("sathish")
# print(names)                      # ['suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish']
#
# names.extend(["kumar","dileep"])
# print(names)                     # ['suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
#
# names.insert(0,"suku")
# print(names)              # ['suku', 'suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
#
#
# # Remove ___________________________________________________________________________________________________________________________________________________
# names=['suku', 'suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
# names.remove("giri")      # giri this a remove
# print(names)              # ['suku', 'suresh', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
#
# names.pop(2)              # murali
# print(names)              # ['suku', 'suresh', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
#
# del names[3]              # nani
# print(names)              # ['suku', 'suresh', 'ravi', 'somu', 'sathish', 'kumar', 'dileep']
#
# names.clear()             # All values clear this a emty list
# print(names)              # []
#
# #cheng value ____________________________________________________________________________________________________________________________________________________
# names=['suku', 'suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
# names[0]="bhanu"
# print(names)             # ['bhanu', 'suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
#
# # Sort _____________________________________________________________________________________________________________________________________________________
# names=['suku', 'suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
# names.sort()
# print(names)              # ['dileep', 'giri', 'kumar', 'murali', 'nani', 'ravi', 'sathish', 'somu', 'suku', 'suresh']
#
# names.sort(reverse=False)
# print(names)              # ['dileep', 'giri', 'kumar', 'murali', 'nani', 'ravi', 'sathish', 'somu', 'suku', 'suresh']
#
# for i in sorted(names):
#     print(i,end=" , ")      # dileep , giri , kumar , murali , nani , ravi , sathish , somu , suku , suresh ,
#
# # Reverse _________________________________________________________________________________________________________________________________________________________________
# names=['suku', 'suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
# names.reverse()
# print(names)      # ['dileep', 'kumar', 'sathish', 'somu', 'nani', 'ravi', 'murali', 'giri', 'suresh', 'suku']
#
# names.sort(reverse=True)
# print(names)        # ['suresh', 'suku', 'somu', 'sathish', 'ravi', 'nani', 'murali', 'kumar', 'giri', 'dileep']
#
# for i in reversed(names):
#     print(names,end=" ")   # 'suku', 'suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep'
#
# # min max __________________________________________________________________________________________________________________________________________________
# names=['suku', 'suresh', 'giri', 'murali', 'ravi', 'nani', 'somu', 'sathish', 'kumar', 'dileep']
# x=min(names)
# y=max(names)
# print(x,y) # dileep suresh
#
# print(max(names))            #suresh
# print(min(names))            #dileep












