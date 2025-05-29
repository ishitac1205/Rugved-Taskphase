#1
"""
class marks:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.average=((self.phy+self.chem+self.math)/3)
        
    def avg(self):
        self.average=((self.phy+self.chem+self.math)/3)
        
    
s1=marks(97,98,99)
print(s1.average)
s1.phy=54
s1.avg()
print(s1.average)"""

#2
class marks:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def average(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

s2=marks(97,98,99)
print(s2.average)
s2.phy=54
print(s2.average)      
