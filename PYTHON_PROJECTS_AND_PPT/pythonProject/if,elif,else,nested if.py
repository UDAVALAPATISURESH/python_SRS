'''
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

                               If statements
These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.

                                    Elif
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

                                    Else
The else keyword catches anything which isn't caught by the preceding conditions.

                                Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

                                   And
The and keyword is a logical operator, and is used to combine conditional statements:

                                    Or
The or keyword is a logical operator, and is used to combine conditional statements:

                                   Not
The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

                                 Nested If
You can have if statements inside if statements, this is called nested if statements.

                              The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass
statement to avoid getting an error.

'''
# #________________________________________________________________________________________________________________________________________________________________________________________________________________________
'''
=> Greater than (a > b):
Checks whether the value of a is greater than the value of b.
Example: 3 > 2 would evaluate to True.
___________________________________________________________________________________________________________________________________________________________________________________________
=> Less than (a < b):
Checks whether the value of a is less than the value of b.
Example: 2 < 3 would evaluate to True.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=> Greater than or equal to (a >= b):
Checks whether the value of a is greater than or equal to the value of b.
Example: 3 >= 3 would evaluate to True.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=> Less than or equal to (a <= b):
Checks whether the value of a is less than or equal to the value of b.
Example: 2 <= 2 would evaluate to True.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=> Equals (a == b):
Checks whether the value of a is equal to the value of b.
Example: 2 == 2 would evaluate to True.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=> Not Equals (a != b):
Checks whether the value of a is not equal to the value of b.
Example: 3 != 2 would evaluate to True.

'''
# # Greater than: (a > b):- ____________________________________________________________________________________________________________________________________________________________________________________
# a = 50
# b = 10
# if a>b:
#     print("a is greater than b")         # a is greater than b

# # Less than: (a < b):- _____________________________________________________________________________________________________________________________________________________________________
# a=10
# b=30
# if a<b:
#     print("b is greater than a")         # b is greater than a

# # Greater than or equal to (a >= b):- _______________________________________________________________________________________________________________________________________________________________________________
# a=100
# b=30
# if a >= b:
#     print("a Greater than or equal to b")
#
# a=30
# b=30
# if a >= b:
#     print("a Greater than or equal to b")

# # Less than or equal to (a <= b):_________________________________________________________________________________________________________________________
# a=30
# b=100
# if a <= b:
#     print("b Greater than or equal to a")
#
# a=30
# b=30
# if a <= b:
#     print("b Greater than or equal to a")

# # Equals (a == b):-______________________________________________________________________________________________________________________________________________________
# a=100
# b=100
# if a == b:
#     print("a equals b")

# # Not Equals (a != b):- _____________________________________________________________________________________________________________________________________________________________________________
# a=30
# b=100
# if a != b:
#     print("a not equals b")

# # And
# a=30
# b=100
# if a or b:
#     print("a not equals b")

##
# a=30
# b=100
# if a and b:
#     print("a not equals b")
#
# a=30
# b=100
# if a is  b:
#     print("a not equals b")

##
# a=30
# b=100
#if a in not  b:
 #   print("a not equals b")


# x = 41
#
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")




# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")


# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
#
#
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")




# # Equals (a == b):- ____________________________________________________________________________________________________________________________________________________________________________________________________________________


# print("Exam results")
# marks = 52
# if marks >= 35:
#     print("You Pass the Exam !")