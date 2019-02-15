T = int(input())

for tc in range(T):
    N = int(input())

    a = list(map(int, input().split()))
    num_max = 0
    num_min = a[0]
    for i in range(N):
        if(a[i] > num_max):
            num_max = a[i]
        if(a[i] < num_min):
            num_min = a[i]
    
    res = num_max - num_min
    print(f"#{tc+1} {res}")