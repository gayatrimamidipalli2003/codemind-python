n=int(input())
s=0
while n:
    s+=n%10
    n//=10
    if n==0 and s>9:
        n=s
        s=0
print(s)