T = int(input())

for i in range(T):
    N = int(input())

    sinsa = 0
    seajong = 0
    ii = 0
    leehwang = 0
    hak = 0
    sunshin = 0
    ssal = 0
    top = 0

    if(N // 50000 > 0):
        a = N // 50000
        N = N - 50000 * (N // 50000) 
        sinsa += a
    
    if(N // 10000 > 0):
        a = N // 10000
        N = N - 10000 * (N // 10000)
        seajong += a

    if(N // 5000 > 0):
        a = N // 5000
        N = N - 5000 * (N // 5000)
        ii += a

    if(N // 1000 > 0):
        a = N // 1000
        N = N - 1000 * (N // 1000)
        leehwang += a

    if(N // 500 > 0):
        a = N // 500
        N = N - 500 * (N // 500)
        hak += a

    if(N // 100 > 0):
        a = N // 100
        N = N - 100 * (N // 100)
        sunshin += a

    if(N // 50 > 0):
        a = N // 50
        N = N - 50 * (N // 50)
        ssal += a

    if(N // 10 > 0):
        a = N // 10
        N = N - 10 * (N // 10)
        top += a

    print(f"#{i+1}")
    print(f"{sinsa} {seajong} {ii} {leehwang} {hak} {sunshin} {ssal} {top}")
