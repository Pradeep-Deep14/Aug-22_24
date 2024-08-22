L = ["Apple", "Apple", "Banana", "Guava"]
element_count = {}

for i in L:
    if i in element_count:
        element_count[i] += 1
    else:
        element_count[i] = 1

# Print the individual counts of elements in L
for i, count in element_count.items():
    print(f"The count of {i} is: {count}")
