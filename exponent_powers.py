A = int(input("Enter the base (A): "))
B = int(input("Enter the exponent (B): "))

result = 1

for _ in range(B):
    result *= A

print("A power B is:", result)
