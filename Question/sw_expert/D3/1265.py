import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    n, p = map(int, input().split())
    money = list(range(1, n+1))
    if(n%p == 0):
        res = (n//p) ** p
    else:
        res = (n//p) ** (p - n%p)
        for i in range(n%p):
            res *= n//p + 1

    print("#{} {}".format(tc+1, res))



