import sys

sys.stdin = open("input.txt", "r")

def find():
    res = []
    for i in range(2**n):
        ss = 0
        for j in range(n):
            if(i & (1 << j) != 0):
                ss += s[j]
        if(ss >= b):
            res.append(ss)
    return res




T = int(input())

for tc in range(T):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))

    ans = list(set(find()))
    minV = max(ans)
    for i in range(len(ans)):
        if(abs(ans[i] - b) >= 0 and abs(ans[i] - b) <= minV):
            minV = abs(ans[i] - b)

    print("#{} {}".format(tc+1, minV))

