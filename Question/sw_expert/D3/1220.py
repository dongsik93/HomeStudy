import sys

sys.stdin = open('input.txt', 'r')

for tc in range(10):
    n = int(input())

    a = []
    for i in range(100):
        a.append(list(map(int, input().split())))

    cnt = 0
    for i in range(100):
        x = 0
        for j in range(100):
            if(a[j][i] == 1):
                x = 1
            elif(a[j][i] == 2 and x == 1):
                cnt += 1
                x = 2

    print(f"#{tc+1} {cnt}")