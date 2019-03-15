n, m = map(int, input().split())

dd = {}
for i in range(n+m):
    word = input()
    if(word not in dd):
        dd[word] = 1
    else:
        dd[word] += 1

cnt = 0
res = []
for k,v in dd.items():
    if(v == 2):
        res.append(k)
        cnt += 1

print(cnt)
print(*sorted(res), sep="\n")