num=int(input("Enter number:"))
for i in range(2,num):
    if(num%2==0):
        print("Not Prime")
        break
else:
    print("Prime")
