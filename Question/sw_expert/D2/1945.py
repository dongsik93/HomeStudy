T = int(input())

for i in range(T):
    N = int(input())

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while(True):
        if(N%2==0):
            N = N / 2
            a = a + 1
        else:
            break
    while(True):
        if(N%3==0):
            N = N / 3
            b = b + 1
        else:
            break
    while(True):
        if(N%5==0):
            N = N / 5
            c = c + 1
        else:
            break
    while(True):
        if(N%7==0):
            N = N / 7
            d = d + 1
        else:
            break
    while(True):
        if(N%11==0):
            N = N / 11
            e = e + 1
        else:
            break

    print(f"#{i+1} {a} {b} {c} {d} {e}")