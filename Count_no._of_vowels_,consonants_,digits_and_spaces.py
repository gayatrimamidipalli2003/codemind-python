s=input()
s=s.lower()
a=b=c=d=0
for i in s:
    if i in 'aeiou':
        a+=1
    elif i in '0123456789': #i.isdigit()
        c+=1
    elif i==' ':
        d+=1
    else:
        b+=1
print('Vowels:',a)
print('Consonants:',b)
print('Digits:',c)
print('White spaces:',d)
    