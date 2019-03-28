def f(n,k,e,c):
    global minV
    if(n == k):
        if(c < minV):
            minV = c
        return
    elif(c >= minV):
        return
    else:
        if(e>0):
            f(n+1, k, e-1, c)
        f(n+1, k, a[n]-1, c+1)

T = int(input())

for tc in range(T):
    a = list(map(int, input().split()))
    cnt = 0
    minV = len(a)
    f(1, a[0], a[1], cnt)
    print("#{} {}".format(tc+1, minV))