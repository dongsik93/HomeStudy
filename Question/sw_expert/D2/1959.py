T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    large = M
    small = N
    if(N > M):
        large = N
        small = M

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sub = large-small
    
    if(len(a) > len(b)):
        a, b = b, a

    max_sum = []
    for j in range(sub+1):
        sum = 0
        for k in range(small):
            x = a[k] * b[k+j]
            sum += x
        max_sum.append(sum)
    
    max_sum.sort(reverse=True)
    print(f"#{i+1} {max_sum[0]}")


