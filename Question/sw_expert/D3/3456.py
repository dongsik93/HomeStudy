T = int(input())
ans = []
for tc in range(T):
    a, b, c, = map(int, input().split())
    res = 0
    if(a == b):
        res = c
    elif(a == c):
        res = b
    elif(b == c):
        res = a
    ans.append(res)

for i in range(T):
    print("#{} {}".format(i+1, ans[i]))