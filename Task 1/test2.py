s=input("enter string:")
s=list(s)
for i in range(2,len(s),3):
    print(ord(s[i]))
    s[i]=" "

s="".join(s)
print(s)