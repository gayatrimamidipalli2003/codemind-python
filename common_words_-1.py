s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
#a=[]
c=0
for i in s1:
    for j in s2:
        if i==j:
            #a.append(i)
            c+=1
#print(len(a))
print(c)