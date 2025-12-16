list1 = eval(input("1 --Enter a list : "))
list2 = eval(input("2 --Enter a list : "))
overlap = False
for lak in list1:
    if lak in list2:
        overlap = True
        break

if overlap:
    print("Overlapped")
else:
    print("Separate")
