n=int(input())
s=0
while 1:
    if n==0 and s>9:
        n=s
        s=0
    elif n==0 and s<10:
        print(s)
        break
    rem=n%10
    s+=rem
    n//=10
