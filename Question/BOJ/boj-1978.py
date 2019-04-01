def prime(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if n % i is 0:
            return 0
    return 1


n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    cnt += prime(i)
print(cnt)