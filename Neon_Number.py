n=int(input())
temp=n
s=n*n
sum=0
while s:
    r=s%10
    sum=sum+r
    s=s//10
if temp==sum:
    print("Neon Number")
else:
    print("Not Neon Number")
    
    
    
    