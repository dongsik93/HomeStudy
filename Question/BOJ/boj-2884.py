h, m = map(int, input().split())

if(m >= 45):
    m = m - 45
else:
    m = 60 - (45 - m)
    if(h-1 >= 0 ):
        h = h-1
    else:
        h = 23

print(h, m)