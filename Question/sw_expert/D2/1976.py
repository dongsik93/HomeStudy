T = int(input())

for i in range(T):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2
    if(m == 60):
        m = 0
        h += 1
    elif(m > 60):
        m -= 60
        h += 1
    if(h > 12):
        h -= 12
    print(f"#{i+1} {h} {m}")
