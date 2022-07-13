x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
sett1=set(a)
sett2=set(b)
for i in sett1:
    if i not in b:
        count+=1
for i in sett2:
    if i not in a:
        count+=1
print(count)
