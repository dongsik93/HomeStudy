import sys

sys.stdin = open('input.txt', 'r')


for tc in range(10):
    a = int(input())
    n = []
    for i in range(100):
        n.append(list(map(int, input().split())))

    width = []
    height = []
    right_sum = 0
    left_sum = 0
    for i in range(100):
        width_sum = 0
        height_sum = 0
        for j in range(100):
            width_sum += n[i][j]
            height_sum += n[j][i]
            if(i == j):
                right_sum += n[i][j]
            if(i+j == 99):
                left_sum += n[i][j]
        width.append(width_sum)
        height.append(height_sum)

    wid_max = max(width)
    height_max = max(height)

    total = []
    total.append(wid_max)
    total.append(height_max)
    total.append(right_sum)
    total.append(left_sum)

    total_max = max(total)
    print(f"#{tc+1} {total_max}")