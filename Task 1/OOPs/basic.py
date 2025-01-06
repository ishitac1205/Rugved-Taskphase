class Student:
    def __init__(self,name):
        print("loading")
        self.name=name
    name= "karan"

s1=Student("Ishan")
print(s1.name)

del s1.name
print(s1.name)
del s1.name
print(s1.name)