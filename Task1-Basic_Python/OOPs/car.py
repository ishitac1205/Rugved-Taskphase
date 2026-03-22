class car:
    def __init__(self):
        self.acc=False
        self.clch=False
        self.brk=False
    
    def start(self):
        self.acc=True
        self.clch=True
        print("car starting..")

s1=car()
s1.start()