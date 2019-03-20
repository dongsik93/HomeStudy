T = int(input())

for tc in range(T):
    y = int(input())
    c, g = [], []
    for i in range(y):
        a, b, = input().split()
        c.append(int(a))
        g.append(int(a)*float(b))

    print(sum(c), end=" ")
    print(round(sum(g)/sum(c),1))
