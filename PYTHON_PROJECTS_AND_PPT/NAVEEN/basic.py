u_list=[10,"Hi",3.14,"Hello"]
u_list[0]=100
print("Forward Index")
print("u_list[0]:",u_list[0])
print("u_list[1]:",u_list[1])
print("u_list[2]:",u_list[2])
print("u_list[3]:",u_list[3])
print("Backward Index")
print("u_list[-1]:",u_list[-1])
print("u_list[-2]:",u_list[-2])
print("u_list[-3]:",u_list[-3])
print("u_list[-4]:",u_list[-4])



list1=[9,6,5,8,1,3,7,4]
 
print (list1)       #printing the complete list
 
print (list1[:-5])  #This will slice the elements from -5 to backward index
 
print (list1[-5:])  #This will slice the elements from -5 to forward index
 
print (list1[:5])   #This will slice the elements from 5 to backward index
 
print (list1[5:])   #This will slice the elements from 5 to forward index
 
print (list1[2:5])  #This willslice the elements in between 2:5
print (list1[-5:-2])  #This willslice the elements in between -5:-2
 
list1[2:5]=[11,12,44] #Modifying  the elements in between 2:5
 
print (list1)       #printing the complete list




u_list=[1,2,3]
print(u_list*1)
print(u_list*2)
print(u_list*3)
print(u_list*4)
