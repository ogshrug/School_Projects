# Input list
lst = eval(input("Enter a list : "))

# Dictionary to store frequencies
freq = {}


for item in lst:
    freq[item] = freq.get(item, 0) + 1


unique_elements = []
duplicate_elements = []

for key, value in freq.items():
    if value == 1:
        unique_elements.append(key)
    else:
        duplicate_elements.append(key)


print("Frequencies of elements:")
for key, value in freq.items():
    print(key, ":", value)

print("\nUnique elements:", unique_elements)
print("Duplicate elements:", duplicate_elements)
