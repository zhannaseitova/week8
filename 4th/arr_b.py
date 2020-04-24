arr= [int(i) for i in input().split()]
arr2 =  filter(lambda x: x%2==0, arr)
print(*arr2)