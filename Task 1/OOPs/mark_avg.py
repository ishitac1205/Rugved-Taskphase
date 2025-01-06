class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def avg(self):
        avg=(self.mark1+self.mark2+self.mark3)/3
        return avg

s1=student("ishita",98,97,96)
print(s1.avg())


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        avg=(ls[0]+ls[1]+ls[2])/3
        return avg

s2=Student("Ishita",[98,96,97])
print(s2.avg)