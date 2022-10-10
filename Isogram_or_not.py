n=input().lower()
l=[]
for i in n:
    if n.count(i)==1:
        l.append(i)
if len(n)==len(l):
    print("True")
else:
    print("False")