s=input()
v='aeiou'
l=[]
for i in s:
    if i in v:
        if i not in l:
            l.append(i)
if len(v)==len(l):
    print("True")
else:
    print("False")