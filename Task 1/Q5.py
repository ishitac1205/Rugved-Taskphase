def fact(n):
    if(n==0 or n==1):
        return 1
    facto= fact(n-1)*n
    return facto

print(fact(5))