n= int(input("Enter a number:"))
t=0

while(n!=0):
    b=n%10
    m=n//10
    c=m%10
    if(b>c):
        p=n//10
        q=m//10
        while(p!=0):
            
            e=p%10
            f=q%10
            if(e<f):
                t+=1
                break
            '''if(e==f):
                t+=1
                break'''
            p=p//10
            q=q//10
            
    '''if(b==c):
        t+=1
        break'''
    n=n//10

if(t==0):
    print("hill")
else:
    print("not hill")
            

        

    