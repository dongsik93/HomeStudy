from itertools import permutations
n, m = map(int, input().split())
a = list(range(1,n+1))
ans = list(permutations(a, m))
for i in range(len(ans)):
    print(*ans[i])
