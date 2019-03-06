import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    n = int(input())

    route = []
    for i in range(n):
        route.append(list(map(int, input().split())))

    p = int(input())
    c = []
    for i in range(p):
        c.append(int(input()))

    print("#{}".format(tc+1), end=" ")

    for k in range(p):
        cnt = 0
        for i in range(n):
            for j in range(1, 2):
                if(route[i][j-1] <= c[k] and c[k] <= route[i][j]):
                    cnt += 1
        print("{}".format(cnt), end=" ")
    print()