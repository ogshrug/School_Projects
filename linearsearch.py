def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


numbers = eval(input("Enter a list : "))
key = int(input("Enter element : "))

result = linear_search(numbers, key)
print(result)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
