n = int(input())
l=list(map(int,input().split()))
expected=sum(range(1,n+1))
actual=sum(l)
missing=expected-actual
print(missing)
