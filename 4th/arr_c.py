arr = [int(i) for i in input().split()]
arr2 = filter(lambda x: x>0, arr)
print(len(list(arr2)))