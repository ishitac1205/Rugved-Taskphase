s= input("Enter a string:")
#string are immutable
ls= list(s)



for i in range(0,len(ls)-1):
    min=i
    for j in range(i+1,len(ls)):
        if ls[min]>ls[j]:
            min=j
    temp=ls[i]
    ls[i]=ls[min]
    ls[min]=temp

#print("".join(ls))

s=""
for i in range(0,len(ls)):
    
    s=s+ls[i]
print(s)

