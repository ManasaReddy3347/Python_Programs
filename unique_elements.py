arr = [1, 2, 3, 2, 1, 4, 5, 4]
seen = set()
unique_elements = []

for element in arr:
    if element not in seen:
        unique_elements.append(element)
        seen.add(element)

for element in unique_elements:
    print(element)
