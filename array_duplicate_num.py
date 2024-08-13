arr = [1, 3, 4, 2, 5, 3]
seen = set()

for num in arr:
    if num in seen:
        print("Duplicate element is:", num)
        break
    seen.add(num)
else:
    print("no duplicates in array")
