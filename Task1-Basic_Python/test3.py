s=input("enter string: ")
w=1
for i in range(0,len(s)-1):
    if(not(s[i].isalpha())):
        if(s[i+1].isalpha()):
            w+=1

print(w)