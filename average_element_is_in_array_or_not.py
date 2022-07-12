n=int(input())
a=list(map(int,input().split()))
sum=c=0
for i in a:
    sum+=i
res=sum//n
if res in a:
    print(True)
else:
    print(False)