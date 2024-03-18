class Student :
    college = "SGS arst college "
    def __init__(self):
        self.marks  = 'marks'
        self.marks1 = 'marks1'
        self.marks2 = 'marks2'
        self.marks3 = 'marks3'

#get method = Accessors antemu
    def get_m(self):
        return  self.marks

    def get_m1(self):
        return  self.marks1

    def get_m2(self):
        return self.marks2

    def get_m3(self):
        return self.marks3

# set method = mutators antamu
    def set_m(self,value):
        self.marks = value


    def set_m1(self,value):
        self.marks1 = value


    def set_m2(self,value):
        self.marks2 = value

    def set_m3(self,value):
        self.marks3 = value

# class method
    @classmethod
    def get_college(cls):
        return cls.college
s1 = Student()
s2 = Student()
print("College name :",Student.get_college())

s1.set_m(52)
print(s1.get_m())

s1.set_m1(68)
print(s1.get_m1())

s1.set_m2(95)
print(s1.get_m2())

s1.set_m3(54)
print(s1.get_m3())

print("")
print("************************************")
print("College name :",Student.get_college())
s2.set_m1(32)
print(s2.get_m1())

s2.set_m (96)
print(s2.get_m())

s2.set_m2 (63)
print(s2.get_m2())

s2.set_m3 (58)
print(s2.get_m3())










