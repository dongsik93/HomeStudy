import sys

input = sys.stdin.readline

ans = []
for _ in range(3):
    n = list(map(int, input().split()))
    cnt = 0
    res = ""
    for i in n:
        if(i == 0):
            cnt += 1

    if(cnt == 1):
        res = "A"
    elif(cnt == 2):
        res = "B"
    elif(cnt == 3):
        res = "C"
    elif(cnt == 4):
        res = "D"
    else:
        res = "E"

    ans.append(res)

print(*ans, sep="\n")
