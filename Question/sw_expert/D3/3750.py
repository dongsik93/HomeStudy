def d_sum(n):
    n = str(n)
    if(len(n) == 1):
        return n
    else:
        s = 0
        for i in n:
            s += int(i)
        return d_sum(s)

T = int(input())
res = []
for tc in range(T):
    n = int(input())
    res.append(d_sum(n))

for tc in range(T):
    print("#{} {}".format(tc+1,res[tc]))

