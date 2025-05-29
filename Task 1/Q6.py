def ana(s):
    c=0
    for i in range(0,len(s)):
        if(s[i]!=s[(len(s)-1-i)]):
            c+=1
    if(c==0):
        return "anagram"
    else:
        return "not anagram"

w= input("enter a string:")
print(ana(w))     
