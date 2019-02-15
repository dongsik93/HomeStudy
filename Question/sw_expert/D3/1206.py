for tc in range(10):
    lens = int(input())
    N = list(map(int, input().split()))

    res = 0
    big = 0
    for i in range(lens):
        if(N[i] - N[i-1] >= 1 and N[i] - N[i-2] >= 1 and N[i] - N[i+1] >= 1 and N[i] - N[i+2] >= 1 ):
            if(N[i-1] > N[i-2]):
                left = N[i-1]
            else:
                left = N[i-2]
            if(N[i+1] > N[i+2]):
                right = N[i+1]
            else:
                right = N[i+2]
            if(left > right):
                big = left
            else:
                big = right
            res += N[i] - big

    print(f"#{tc+1} {res}")