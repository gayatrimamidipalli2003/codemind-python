def not_prime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return True
    else:
        return False
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if not_prime(i):
            c+=1
print(c+1)