'''
                                     Dictionary :
* Dictionaries are used to store data values in key:value pairs.
* A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
* Dictionaries are written with curly brackets, and have keys and values:


Method                                                     Description


update()	                                         Updates the dictionary with the specified key-value pairs

______________________________________________________________________________________________________________________________
setdefault()	                                     Returns the value of the specified key. If the key does not exist:
                                                     insert the key, with the specified value
______________________________________________________________________________________________________________________________________

copy()	                                             Returns a copy of the dictionary

fromkeys()	                                         Returns a dictionary with the specified keys and value

get()	                                             Returns the value of the specified key

items()	                                             Returns a list containing a tuple for each key value pair

keys()	                                             Returns a list containing the dictionary's keys

values()	                                         Returns a list of all the values in the dictionary

pop()	                                             Removes the element with the specified key

popitem()	                                         Removes the last inserted key-value pair

clear()	                                             Removes all the elements from the dictionary

'''

# # update() ___________________________________________________________________________________________________________________________________________________________________________________________________________
# my = {
#     'name':"suresh",
#     'age':20,
#     'adess':"tirupati",
#     'mobile no' : 7997854712,
# }
# my.update({"first name":"udavalapati"})
# print(my)   # {'name': 'suresh', 'age': 20, 'adess': 'tirupati', 'mobile no': 7997854712, 'first name': 'udavalapati'}

# # setdefault()_____________________________________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name': "UDAVALAPATI",
#     'Last_name': "SURESH",
#     'Age': 20,
#     'City': "Mopur"
# }
# x = my.setdefault("Age",21)
# print(x)      # 20
# print(my)    # {'First_name': 'UDAVALAPATI', 'Last_name': 'SURESH', 'Age': 20, 'City': 'Mopur'}

# # copy()_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name':"UDAVALAPATI",
#     'Last_name' :"SURESH",
#     'Age'       :20,
#     'City'      :"Mopur"
# }
# my_detail = my.copy()
# print(my_detail)                  # {'First_name': 'UDAVALAPATI', 'Last_name': 'SURESH', 'Age': 20, 'City': 'Mopur'}

# # fromkeys()__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________-
# my = {
#     'First_name':"UDAVALAPATI",
#     'Last_name' :"SURESH",
#     'Age'       :20,
#     'City'      :"Mopur"
# }
# my.fromkeys("Age")
# print(my)                          # {'First_name': 'UDAVALAPATI', 'Last_name': 'SURESH', 'Age': 20, 'City': 'Mopur'}

# # get()___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name': "UDAVALAPATI",
#     'Last_name': "SURESH",
#     'Age': 20,
#     'City': "Mopur"
# }
# x = my.get("Age")
# print(x)                    # 20

# # items()___________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name': "UDAVALAPATI",
#     'Last_name': "SURESH",
#     'Age': 20,
#     'City': "Mopur"
# }
# x = my.items()
# print(x)        # dict_items([('First_name', 'UDAVALAPATI'), ('Last_name', 'SURESH'), ('Age', 20), ('City', 'Mopur')])

# # keys()_______________________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name': "UDAVALAPATI",
#     'Last_name': "SURESH",
#     'Age': 20,
#     'City': "Mopur"
# }
# x = my.keys()
# print(x)                       # dict_keys(['First_name', 'Last_name', 'Age', 'City'])

# # values()________________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name': "UDAVALAPATI",
#     'Last_name': "SURESH",
#     'Age': 20,
#     'City': "Mopur"
# }
# x = my.values()
# print(x)        # dict_values(['UDAVALAPATI', 'SURESH', 20, 'Mopur'])
# print(my)       # {'First_name': 'UDAVALAPATI', 'Last_name': 'SURESH', 'Age': 20, 'City': 'Mopur'}

# # pop()____________________________________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name': "UDAVALAPATI",
#     'Last_name': "SURESH",
#     'Age': 20,
#     'City': "Mopur"
# }
# x = my.pop("Age")
# print(x)                       #20
# print(my)                      # {'First_name': 'UDAVALAPATI', 'Last_name': 'SURESH', 'City': 'Mopur'}

# # popitem()______________________________________________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name': "UDAVALAPATI",
#     'Last_name': "SURESH",
#     'Age': 20,
#     'City': "Mopur"
# }
# x = my.popitem()
# print(x)                      # ('City', 'Mopur')
# print(my)                     # {'First_name': 'UDAVALAPATI', 'Last_name': 'SURESH', 'Age': 20}

# # clear()_____________________________________________________________________________________________________________________________________________________________
# my = {
#     'First_name': "UDAVALAPATI",
#     'Last_name': "SURESH",
#     'Age': 20,
#     'City': "Mopur"
# }
# x = my.clear()
# print(x)           # None
# print(my)          # {} Emty






























