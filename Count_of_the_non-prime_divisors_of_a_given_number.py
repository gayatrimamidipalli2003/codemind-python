def not_prime(n):
    if n==1:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    else:
        return False
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and not_prime(i):
        c+=1
print(c)
    