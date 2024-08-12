a=[8,23,7,67,784,98]
print(a)
n=len(a)
max=a[0]
for m in range(1,n):
    if a[m]>max:
        max=a[m]
print("Largest element:",max)
