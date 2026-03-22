num= int(input("Enter credit card no.:"))
ls=list()

while num>0:
    b=num%10
    ls.append(b)
    num=num//10
ls.reverse()
print(ls)

for i in range(len(ls)-2,-1,-2):
    
    ls[i]=ls[i]*2
    sum=0
    if(ls[i]>9):
        p=ls[i]
        while(p>0):
            b=p%10
            sum=sum+b
            p=p//10
        ls[i]=sum


sum1=0
for i in range(0,len(ls)):
    sum1=sum1+ls[i]

if(sum1%10==0):
    print("valid number")
else:
    print("invalid number")