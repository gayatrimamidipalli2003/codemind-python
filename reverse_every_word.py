def rev(n):
    return n[::-1]
s=input()
s=s.split()
for i in s:
    r=rev(i)
    print(r,end=' ')