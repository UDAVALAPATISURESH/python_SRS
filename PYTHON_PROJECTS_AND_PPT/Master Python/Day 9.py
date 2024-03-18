# 1 Create a class to represent a Student with attributes like name, age, and grades.
# class Student :
#     def __init__(self,name,age,greades):
#         self.name = name
#         self.age = age
#         self.greades = greades
#     def stu(self):
#         print("Student name : " ,self.name)
#         print("Student age :", self.age)
#         print("Student greades :",self.greades)
# stu_obj = Student(name = "suresh",age =20 , greades = 7.0)
# stu_obj.stu()

# # 2 .Given a CSV file with employee details (name, position, salary), create a class to represent an Employee7
# class Employee :
#     def __init__(self,name,position,salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
#     def employee(self):
#         print("Employee name     : ",self.name)
#         print("Employee position : ",self.position)
#         print("Employee salary   : ",self.salary)
# Ey = Employee("Suresh","python Developer",1500)
# Ey.employee()

# # 3 Implement a program that simulates a basic bank account using a BankAccount class7
# class BankAccount:
#     def __init__(self,account_holder,account_number,balance):
#         self.account_holder = "account_holder"
#         self.account_number = account_number
#         self.balance = balance
#     # def acc(self):
#     #     print("Name :",self.account_holder)
#     # def acccoun(self):
#     #     print("account_number :",self.account_number)
#     def deposit(self,amount):
#         if amount > 0 :
#             self.balance += amount
#             print("deposit  New balance:",self.balance)
#
#         else:
#             print("Invalid withdrawal amount. Please enter a positive value.")
#
#     def withdraw (self,amount):
#         if  0 < amount <= self.balance:
#             self.balance -= amount
#             print("Withdrew After . New balance:" ,self.balance)
#
#         else :
#             print("no amount")
#     def balance_check(self):
#         print(f"Current balance for {self.balance}")
#
# bank = BankAccount(account_holder="Suresh",account_number = 7997854712, balance = 500)
# bank.deposit(200)
# bank.withdraw(100)
# bank.balance_check()

# # 4 Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle


# # 5 Create a class to represent a Car with attributes like make, model, and year7
# class Mobile:
#     def __init__(self,name,model,ram,rom,year):
#         self.Name = name
#         self.Model = model
#         self.Ram = ram
#         self.Rom = rom
#         self.year = year
#     def mobile(self):
#         print("NAME  : ",self.Name)
#         print("MODEL : ",self.Model )
#         print("RAM   : ",self.Ram)
#         print("ROM   : ",self.Rom)
# shop = Mobile("Redmi","Redmi 8","4GB","64",2020)
# shop.mobile()

# # 6 Given a JSON file with customer data, create a Customer class to store and manipulate the data
#import json
# class Customer :
#     def __init__(self,customer_id,name,email,address):
#         self.customer_id = customer_id
#         self.name = name
#         self.email = email
#         self.address = address
#     def customer(self):
#         print("COSTOMER ID   : ",self.customer_id)
#         print("NAME          : ",self.name)
#         print("EMAIL         : ",self.email)
#         print("ADDRESS       : ",self.address)
#
# customer_data = {
#     'customer_id' : 7998,
#     'name' : "Suresh",
#     'email' : "luckysuresh494@gmail.com",
#     'address' : 'tirupati'
# }
# customer1=Customer(**customer_data)
# customer1.customer()

# # 7 Write a program that uses a Person class to keep track of a person's name, age, and address
# class Person :
#     def __init__(self,name,age,mobile_number,address):
#         self.name = name
#         self.age = age
#         self.mobile_number = mobile_number
#         self.address = address
#
#     def person_info(self):
#         print("NAME          : ",self.name)
#         print("AGE           : ",self.age)
#         print("MOBILE_NUMBER : ",self.mobile_number)
#         print("ADDRESS       : ",self.address)
#
# p1 = Person (name="SURESH",age=20,mobile_number=7997854712,address="tirupati")
# p1.person_info()

# # 8 Implement a program that uses a Circle class to calculate the area and circumference of multiple circles

# # 9 Given a CSV file with product details (name, price, quantity), create a Product class to manage the data
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def product_details(self):
        print("NAME     : ",self.name)
        print("PRICE    : ",self.price)
        print("QUANTITY : ",self.quantity)
product1 = Product(name = "BIRIYNI",price = 299.1,quantity = 1.02 )
product1.product_details()






















































