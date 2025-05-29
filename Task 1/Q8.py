s=input("Enter sequence:")
c=0

for i in range(1,(len(s)//2)+1):
    a=0
    b=i
    while(b+i<=len(s)):
        if(s[a:b]!=s[a+i:b+i]):
            c=1
            break
        else:
            if(b+2*i>len(s)):
                if((b+i)<len(s)):
                    c=1
                    break
            
            c=0
        a=a+i
        b=b+i
    if(c==0):
        step_length=i
        break
    else:
        continue

ls=list()
p=0
a=0
b=i
if(c==0):
    while(b<=len(s)):
        ls.append(s[a:b])
        a=a+i
        b=b+i
        p+=1
    print(ls)


else:
    print("No pattern found")




