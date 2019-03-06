T = int(input())

for tc in range(T):
    a = list(input())
    b = list(input())
    c = list(input())
    d = list(input())
    e = list(input())
    print("#{}".format(tc+1), end=" ")
    for i in range(15):
        if(len(a)-1 >= i):
            print(a[i], end="")
        if(len(b) - 1 >= i):
            print(b[i], end="")
        if(len(c) - 1 >= i):
            print(c[i], end="")
        if(len(d) - 1 >= i):
            print(d[i], end="")
        if(len(e) - 1 >= i):
            print(e[i], end="")
    print()