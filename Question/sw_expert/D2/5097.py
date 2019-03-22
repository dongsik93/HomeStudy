T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    a = m % n
    print("#{} {}".format(tc+1, num[a]))