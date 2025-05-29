#1
"""
class a:
    name="anonymous"
    def changename(self,name):
        self.__class__.name=name
        return self.__class__.name

s1=a()
print(s1.changename("ishan"))"""

#2
"""
class b:
    name="anonymous"
    def change_name(self,name):
        b.name=name
        return b.name
s2=b()
print(s2.name)
print(b.name)
print(s2.change_name("Ishita"))
print(s2.name)
print(b.name)"""

#3
class c:
    name="anonymous"
    @classmethod
    def change_name(cls,name):
        cls.name=name

s3=c()
print(s3.name)
s3.change_name("medhini")
print(s3.name)
