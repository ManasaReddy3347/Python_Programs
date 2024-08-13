N = int(input("Enter a number: "))
sum_of_cubes = sum(int(digit) ** 3 for digit in str(N))

if sum_of_cubes == N:
    print(N, "is an Armstrong number")
else:
    print(N, "is not an Armstrong number")
