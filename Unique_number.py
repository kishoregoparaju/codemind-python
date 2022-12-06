n = int(input())
one,two,three,four,five,six,seven,eight,nine=0,0,0,0,0,0,0,0,0
while n:
    if n%10==1:
        one+=1
    elif n%10==2:
        two+=1
    elif n%10==3:
        three+=1
    elif n%10==4:
        four+=1
    elif n%10==5:
        five+=1
    elif n%10==6:
        six+=1
    elif n%10==7:
        seven+=1
    elif n%10==8:
        eight+=1
    elif n%10==9:
        nine+=1
    n//=10
if one<2 and two<2 and three<2 and four<2 and five<2 and six<2 and seven<2 and eight<2 and nine<2:
    print("Unique Number")
else:
    print("Not Unique Number")