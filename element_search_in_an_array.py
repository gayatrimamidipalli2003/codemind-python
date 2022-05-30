n=int(input())
a=list(map(int,input().split()))
x=int(input())
for i in a:
    if i==x:
        print(True)
        break
else:
    print(False)
