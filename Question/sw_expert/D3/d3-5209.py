def per(index,n,s):
    global minV
    if(index == n):
        if(s < minV):
            minV = s
    elif (s >= minV):  # 백트래킹
        return
    for i in range(n):
        if(check[i] == 0):
            check[i] = 1
            per(index+1, n, s+arr[index][i])
            check[i] = 0


T = int(input())

for tc in range(T):
    n = int(input())
    arr = []
    s = 0
    check = [0 for i in range(n)]
    for i in range(n):
        arr.append(list(map(int, input().split())))
    minV = 10000000
    per(0, n, s)
    print("#{} {}".format(tc+1, minV))