T = int(input())
res = []
for _ in range(T):
    a, b, c, d = map(int, input().split())
    if(a/b < c/d):
        res.append("BOB")
    elif(a/b > c/d):
        res.append("ALICE")
    else:
        res.append("DRAW")
for tc in range(T):
    print("#{} {}".format(tc+1, res[tc]))