# def sayHello(name,age):
#     print(f"Hello {name}  your age {age}")
# sayHello("suresh",20)
# print("*****")
# sayHello("muni",20)

# def add(a,n):
#     result =  a+n
#     print(result)
# add(20,62)

# def mult(*x):
#     result = 0
#     for i in x:
#         result += i
#     print("result",result)
#     print(x[0])
#     print(x[3])
# mult(10,25,3,5,2,8,38,85,75)
# mult(45,15,82,46)

# def deail(name,age):
#     print("Name   :",name)
#     print("My age :",age)
# deail("suresh",20)

# def deails(name,age,mobileno,country = 'india'):
#     print('My name          : ' ,name)
#     print('My Age           : ' ,age)
#     print('iam form         : ' ,country)
#     print('my mobile number : '   ,mobileno)
#
# deails(name="suresh",age=20,mobileno=7997854712)


# def deails(name,age,mobileno,country = 'india'):
#     print('My name          : ' ,name)
#     print('My Age           : ' ,age)
#     print('iam form         : ' ,country)
#     print('my mobile number : '   ,mobileno)
#
# deails(name="suresh",age=20,mobileno=7997854712)

# def add(*x):
#     num = 0
#     vil = 123
#     for i in x:
#         num += i
#     return num , vil
# sum, vil = add(12,5,86,78,58,52)
# print(sum,vil)

# Arbitrary keyword Arguments [**kwargs] _______________________________________________________________________________________________________________________________________
def names(**self):
    