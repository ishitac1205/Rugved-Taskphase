class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"+",self.img,"i")
    
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)

num1=Complex(1,2)
num2=Complex(3,4)
num3=num1+num2
num3.show()