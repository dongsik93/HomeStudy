import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    square = [[0] * 10 for i in range(10)]
    count = 0
    num = int(input())
    for n in range(num):
        r1, c1, r2, c2, color = map(int, input().split())
        row = r2 - r1
        col = c2 - c1
        for i in range(row + 1):
            for j in range(col + 1):
                if square[r1+i][c1+j] == 0:
                    square[r1+i][c1+j] = color
                else:
                    count += 1

    print(f'#{t+1} {count}')
