import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(N)]

    sum_arr = []
    for x in range(N-M+1):
        for i in range(N-M+1):
            sum = 0
            for j in range(M):
                for k in range(M):
                    sum += arr[j+x][k+i]
            sum_arr.append(sum)

    print(f"#{tc+1} {max(sum_arr)}")