s= input("Enter string:")
'''s=list(s)
for i in range(0,len(s)//2):
    temp=s[i]
    s[i]=s[len(s)-1-i]
    s[len(s)-1-i]=temp

s= " ".join(s)
print(s)'''

print(s[::-1])