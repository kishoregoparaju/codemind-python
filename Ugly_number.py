n=int(input())
temp=n
a=0
while temp!=1:
    if temp%2==0:
        temp = temp//2
        
    elif temp%3==0:
        temp=temp//3
        
    elif temp%5==0:
        temp=temp//5
    else:
        a+=1
        break
if a==1:
    print("Not Ugly Number")
else:
    print("Ugly Number")