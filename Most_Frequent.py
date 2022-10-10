n=int(input())
arr=list(map(int,input().split()))
one=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0
zero=0
for i in range(0,n):
    if arr[i]==1:
        one+=1
    elif arr[i]==2:
        two+=1
    elif arr[i]==3:
        three+=1
    elif arr[i]==4:
        four+=1
    elif arr[i]==5:
        five+=1
    elif arr[i]==6:
        six+=1
    elif arr[i]==7:
        seven+=1
    elif arr[i]==8:
        eight+=1
    elif arr[i]==9:
        nine+=1
    elif arr[i]==0:
        zero+=1
if one>=zero and one>=two and one>=three and one>=four and one>=five and one>=six and one>=seven and one>=eight and one>=nine:
    print("1")
elif two>=zero and one<=two and two>=three and two>=four and two>=five and two>=six and two>=seven and two>=eight and two>=nine:
    print("2")
elif three>=zero and three>=two and one<=three and three>=four and three>=five and three>=six and three>=seven and three>=eight and three>=nine:
    print("3")
elif four>=zero and four>=two and four>=three and one<=four and four>=five and four>=six and four>=seven and four>=eight and four>=nine:
    print("4")
elif five>=zero and five>=two and five>=three and five>=four and one<=five and five>=six and five>=seven and five>=eight and five>=nine:
    print("5")
elif six>=zero and six>=two and six>=three and six>=four and six>=five and one<=six and six>=seven and six>=eight and six>=nine:
    print("6")
elif seven>=zero and seven>=two and seven>=three and seven>=four and seven>=five and seven>=six and one<=seven and seven>=eight and seven>=nine:
    print("7")
elif eight>=zero and eight>=two and eight>=three and eight>=four and eight>=five and eight>=six and eight>=seven and one<=eight and eight>=nine:
    print("8")
elif nine>=zero and nine>=two and nine>=three and nine>=four and nine>=five and nine>=six and nine>=seven and nine>=eight and one<=nine:
    print("9")