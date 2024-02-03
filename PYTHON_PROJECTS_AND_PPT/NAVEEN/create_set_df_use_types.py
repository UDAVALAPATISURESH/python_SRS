my_set_using_list = set(['one', 'two', 'nine', 33, 13])
my_set_using_tuple = set(("alpha", "beta", "gamma"))
print("set using list")
print(my_set_using_list)
print("set using tuple")
print (my_set_using_tuple)


my_set = {1, 2, 3, 4}
print(my_set)

myset1={1,2,3,4,5}
print(1 in myset1)

myset1.update(my_set)

print(myset1)

l=[1,2,2,3,3,4,4,5,5,6,6]

l1=[]

for i in l:
    if i not in l1:
        l1.append(i)
print(l1)