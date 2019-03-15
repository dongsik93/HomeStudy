arr = []
for i in range(28):
    arr.append(int(input()))

arr_2 = list(range(1,31))
res = set(arr_2) - set(arr)
print(*sorted(res), sep="\n")