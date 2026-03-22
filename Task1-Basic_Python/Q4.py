s1= input("Enter string:")
s1= list(s1)

for i in range(0,len(s1)-1):
    min=i
    for j in range(i+1,len(s1)):
        if(s1[min]>s1[j]):
            min=j
    temp=s1[i]
    s1[i]=s1[min]
    s1[min]=temp

print("sorted string is ","".join(s1))