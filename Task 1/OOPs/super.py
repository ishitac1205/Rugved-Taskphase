class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car is starting:")
    @staticmethod
    def stop():
        print("car is stopping:")
    
class toyota(car):
    def __init__(self,colour,type):
        #but how to put this type in parent class. call parent class constructor in toyota
        self.col=colour
        super().__init__(type)

s1=toyota("blue","diesel")
print(s1.type)
