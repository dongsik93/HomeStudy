T = int(input())

for tc in range(T):
    L, U, X = map(int, input().split())
    res = -1
    if(X < L):
        res = L - X
    elif(X >= L and X <= U):
        res = 0
    print("#{} {}".format(tc+1, res))