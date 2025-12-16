

L = eval(input("Enter a list : "))
LST=list(L)
LST.sort()
l = len(LST)
key = int(input("Enter element :"))
start = 0
end = l - 1

while start <= end:
    men = (start + end) // 2
    if LST[men] > key:
        end = men - 1
    elif LST[men] < key:
        start = men + 1
    else:
        posi = men
        break
else:
    posi = -1

if posi == -1:
    print("Element not found")
else:
    print("Element found at position", posi)
    print(LST)
