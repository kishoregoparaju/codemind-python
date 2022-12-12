n,d=map(int,input().split())
l=len(str(n))
print(abs(n%(10**d)-n//(10**(l-d))))
