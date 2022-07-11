n=int(input())
for i in range(n):
    s=input()
    l=len(s)
    if s==s[::-1] and l%2==0:
        print('YES EVEN')
    elif s==s[::-1] and l%2!=0:
        print('YES ODD')
    else:
        print('NO')