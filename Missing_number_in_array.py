n=int(input())
for i in range(0,n):
    t=int(input())
    a=list(map(int,input().split()))
    for j in range(1,t+1):
        if j not in a:
            print(j)
            break
            