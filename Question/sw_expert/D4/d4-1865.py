import sys

sys.stdin = open("input.txt", "r")

def per(index, n, s):
    global maxV
    if(index == n):
        if(s > maxV):
            maxV = s
    elif(s <= maxV):
        return
    for i in range(n):
        if(check[i] == 0):
            check[i] = 1
            per(index+1, n, s*arr[index][i])
            check[i] = 0

T = int(input())

for tc in range(T):
    n = int(input())
    arr = []
    check = [0 for i in range(n)]
    arr = [[0] * n for i in range(n)]

    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(n):
            arr[i][j] = a[j] / 100

    maxV = 0
    per(0, n, 1)
    maxV = maxV * 100
    print("#{}".format(tc+1), end=" ")
    print(format(round(maxV,6),"0.6f"))
