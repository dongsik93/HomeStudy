T = int(input())
for tc in range(T):
    hp1, mp1, at1, de1, hp2, mp2, at2, de2, = map(int, input().split())

    if(hp1+hp2 < 1):
        hp = 1
    else:
        hp = hp1 + hp2

    if(mp1+mp2 < 1):
        mp = 1
    else:
        mp = mp1 + mp2

    if(at1+at2 < 0):
        at = 0
    else:
        at = at1 + at2

    de = de1 + de2


    res = hp + 5*mp + 2*at + 2*de
    print(res)