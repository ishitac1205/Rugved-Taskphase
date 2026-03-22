s= input("Enter text:")
c=0
w=1
n=0

for i in range(0,len(s)):
    if((s[i]>="A" and s[i]<="Z") or (s[i]>="a" and s[i]<="z")):
        c+=1

    if(s[i]=="."):
        n+=1

    if(not((s[i]).isalpha())):
        if(i==len(s)-1):
            break
        elif((s[i+1]).isalpha()):
            w+=1

'''coleman liau formula for readability
CLI= 0.0589*(avg no. of char per 100 words)-0.296*(avg no. of words per sentence per 100 words )-15.8'''

cli= (5.89*c/w)-(29.6*n/w)-15.8
print("Grade level is",cli)




    



   

