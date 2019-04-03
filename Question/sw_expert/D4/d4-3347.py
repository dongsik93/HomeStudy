T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    res = [0]*n

    for i in range(m):
        for j in range(n):
            if(bi[i] >= ai[j]):
                res[j] += 1
                break

    print("#{} {}".format(tc+1, res.index(max(res))+1))


