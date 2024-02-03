items=["fruits","veggies","dry","a"] #created list with strings

list1=[1,2,3]
list2=["a","b","c"]
print (items)
items.append(5)       #added the element at end of the list as number
print (items)
items.append("sports") #added the element at end of the list as string
print(items)
items.insert(3,5.6)
print (items)
items.insert(1,'start')
print (items)
print (list1)
print (list2)
list1.extend(list2)
print (list1)
items.remove("a")
print (items)
#items.remove(6)
#print (items)
print(items.pop())
print (items)
print ("1st element is",items.pop(2))
print (items)
items.clear()
print (items)
