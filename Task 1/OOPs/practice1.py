class employee:
    def __init__(role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal
    def showdetails(self):
        print("role=",self.role)
        print("department is",self.dep)
        print("salary is",self.sal)

class engineer(employee):
    def __init__(self,name,age,role,dep,sal):
        self.name=name
        self.age=age
        super().__init__(role,dep,sal)

s1=engineer("ishu",19,"stu","cse",1234)
s1.showdetails()