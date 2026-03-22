class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"+",self.img,"i")

    """def mul(self,num5):
        newreal= (self.real*num5.real)-(self.img*num5.real)
        newimg= (self.img*num2.real)+(self.real*num2.img)
        return complex(newreal,newimg)"""

    def __mul__(self,num5):
        newreal= (self.real*num5.real)-(self.img*num5.real)
        newimg= (self.img*num2.real)+(self.real*num2.img)
        return complex(newreal,newimg)

num1=complex(1,2)
num2=complex(3,4)
num3=num1*num2
num3.show()