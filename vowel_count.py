n=input()
n=n.lower()
c=0
for i in n:
    if i in 'aeiou':
        c+=1
print(c)