class user:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def print_pass(self):
        print(self.__acc_pass)

    @staticmethod
    def __hello():
        print("hello")
    def welcome(self):
        self.__hello()
        


s1= user("1234","abcd")
print(s1.acc_no) 
s1.print_pass()

s1.welcome()
