n = int(input())
while n:
    n-=1
    n1 = int(input())
    temp=n1
    rev=0
    while temp:
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if rev==n1:
        print(True)
    else:
        print(False)