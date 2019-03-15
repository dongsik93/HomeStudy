score = []
for i in range(8):
    score.append(int(input()))

res = {}
for idx, v in enumerate(score,1):
    res[v] = idx

cnt = 0
sums = 0
ans = []
for i in sorted(res, reverse=True):
    sums += i
    ans.append(res[i])
    cnt += 1
    if(cnt == 5):
        break

print(sums)
print(*sorted(ans), sep=" ")