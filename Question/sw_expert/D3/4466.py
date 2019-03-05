T = int(input())

for tc in range(T):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    s = 0
    for i in range(k):
        s += score[i]
    print("#{} {}".format(tc+1, s))
