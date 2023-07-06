n=int(input())
m=int(input())
rev=0
for i in range(n,m+1):
    t=i
    rev=0
    while(t!=0):
        r=t%10
        rev=rev*10+r
        t=t//10
    if(i==rev):
        print(i,end=" ")