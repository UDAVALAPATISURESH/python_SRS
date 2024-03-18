class Student :
    college = "SGS Asrt College"
    def __init__(self):
        self.marks1 = 'marks1'
        self.marks2 = 'marks2'
        self.marks3 = 'marks3'

# Get method_______________________________________________________________________________________________

    def get_m1(self):
        return  self.marks1
    def get_m2(self):
        return  self.marks2
    def get_m3(self):
        return  self.marks3

# set method____________________________________________________________________________________________________

    def set_m1(self,value):
        self.marks1=value

    def set_m2(self,value):
        self.marks2 = value

    def set_m3(self,value):
        self.marks3 = value

# class method   ___________________________________________________________________________________________________________________

    @classmethod
    def get_college(cls):
        return cls.college

# static method __________________________________________________________________________________
    @staticmethod
    def sayhell():
        print("Helllo suresh")

print("College name : " + Student.get_college()) #class method

Student.sayhell() # static method

s1 = Student()
s2 = Student()

s1.set_m1(56)
s1.set_m2(62)
s1.set_m3(78)
print("")
print(s1.get_m1())
print(s1.get_m2())
print(s1.get_m3())

s2.set_m1(10)
s2.set_m2(40)
s2.set_m3(90)
print("")
print(s2.get_m1())
print(s2.get_m2())
print(s2.get_m3())