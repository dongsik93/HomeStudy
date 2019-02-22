T = int(input())

for tc in range(T):
    n, k = map(int, input().split())

    arr = list(range(1,13))
    N = len(arr)
    cnt = 0

    for i in range(2**N):
        s = []
        for j in range(N):
            if(i & (1 << j) != 0):
                s.append(arr[j])
        if(sum(s) == k and len(s) == n):
            cnt += 1    
    print(f"#{tc+1} {cnt}")
