class bottle:
    size="1L"
    hold="water"

class tupper(bottle):
    def info(self):
        print(self.size,"+",self.hold)
    def comment(self):
        print("Good bottle")

class colour(tupper):
    def __init__(self,col):
        self.col=col
    
    def last(self):
        self.comment()
        print("of size",self.size,"and colour",self.col,"and holds",self.hold)

s1=colour("blue")
s1.info()
s1.comment()
s1.last()