T = int(input())

for tc in range(T):
    n = int(input())
    block = list(map(int, input().split()))

    res = 0
    down = 0
    up = 0
    ss = 0
    for i in range(1, n):
        if(block[i-1] < block[i]):
            ups = block[i] - block[i-1]
            if(ups > up ):
                up = ups
        elif(block[i-1] > block[i]):
            downs = block[i-1] - block[i]
            if(downs > down):
                down = downs
        elif(block[i-1] == block[i]):
            ss += 1

    if(ss == n-1):
        down, up = 0, 0
    print("#{} {} {}".format(tc+1, up, down))
