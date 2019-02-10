T = int(input())

for i in range(T):
    n = []
    ans = 1
    for j in range(9):
        n.append(list(map(int, input().split())))
    

    for j in range(9):
        b = []
        c = []
        for k in range(9):
            if(n[j][k] not in b):
                b.append(n[j][k])
            if(n[k][j] not in c):
                c.append(n[k][j])
        if(len(b) != 9):
            ans = 0
        if(len(c) != 9):
            ans = 0

    for l in range(0,9,3):
        a = []
        for j in range(l,3+l):
            for k in range(l,3+l):
                if(n[j][k] not in a):
                    a.append(n[j][k])
        if(len(a) != 9):
            ans = 0            

    print(f"#{i+1} {ans}")