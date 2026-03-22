#ceasers cipher
key= int(input("Enter key:"))
s= input("Enter string:")

s=list(s)
for i in range(0,len(s)):
    if(ord(s[i])>=65 and ord(s[i])<=90):
        val=ord(s[i])
        s[i]=chr(val+key)
        if((val+key)>90):
            s[i]=chr(val+key-90-1+65)
    
    if(ord(s[i])>=97 and ord(s[i])<=122):
        val=ord(s[i])
        s[i]=chr(val+key)
        if((val+key)>122):
            s[i]=chr(val+key-122-1+97)
str1=""
for i in range(0,len(s)):
    str1=str1+s[i]

print("Encrypted string:")
print(str1)