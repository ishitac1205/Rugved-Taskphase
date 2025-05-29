def fib(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    term=fib(n-1)+fib(n-2)
    return term

num= int(input("no. of terms: "))
for i in range(1,num+1):
    print(fib(i))