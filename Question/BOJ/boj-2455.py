a = [0]
maxV = 0

for i in range(4):
    out, ins = map(int, input().split())
    if(out != 0):
        a[0] -= out
        a[0] += ins
    else:
        a[0] += ins
    if(a[0] > maxV):
        maxV = a[0]

print(maxV)