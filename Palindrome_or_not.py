def pali(n):
    b=n[::-1]
    if n==b:
        return 1
    else:
        return 0
n=input()
n=n.lower()
if pali(n):
    print(True)
else:
    print(False)