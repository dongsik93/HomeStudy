T = int(input())

for tc in range(T):
    n, m = map(int, input().split())

    num = list(map(int, input().split()))
    
    num_sum = 0
    ans = []
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += num[j+i]
        ans.append(sum)
    print(f"#{tc+1} {max(ans) - min(ans)}")