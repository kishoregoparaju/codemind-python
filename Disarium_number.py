n=int(input())
temp=n
e=n
s=0
c=0
while(n!=0):
    c+=1
    r=n%10
    n=n//10
while(temp!=0):
    r1=temp%10
    p=r1**c
    s+=p
    temp = temp//10
    c=c-1
if s==e:
    print(True)
else:
    print(False)