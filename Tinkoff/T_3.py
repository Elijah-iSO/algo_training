n, m = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]

change_list = []
for debt in range(1, m+1):
    print('debt', debt)
    change = debt
    for present in prices:
        print('present', present)
        if present <= change:
            change -= present
            print('change', change)

    change_list.append(change)

print(max(change_list))
