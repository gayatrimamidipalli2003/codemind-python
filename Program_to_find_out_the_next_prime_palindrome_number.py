def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
def pali(n):
    temp=n
    rev=0
    while n:
        rev=rev*10+(n%10)
        n//=10
    if rev==temp and prime(rev):
        return 1
        
n=int(input())
res=n+1
while res:
    if pali(res):
        print('%d'%res)
        break
    else:
        res+=1
    