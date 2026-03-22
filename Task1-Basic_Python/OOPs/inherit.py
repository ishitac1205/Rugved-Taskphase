class car:
    def __init__(self,colour,seats):
        self.col=colour
        self.seats=seats

    def concat(self):
        print(self.col,"+",self.seats)

class maruti(car):
    def __init__(self,tyres):
        self.tyres=tyres
    
    def info(self):
        print(self.col)

    def check(self):
        self.concat()
        print("*********")

s1= maruti(4)
print(s1.tyres)
print(s1.col)


