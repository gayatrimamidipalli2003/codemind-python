s=input()
se=input()
c=0
for i in s:
    if i==se:
        c+=1
if c==0:
    print('-1')
else:
    print(c)