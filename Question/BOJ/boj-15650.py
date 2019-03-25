from itertools import combinations

n, m = map(int, input().split())
a = list(range(1,n+1))
for i in list(combinations(a, m)):
    print(*i)