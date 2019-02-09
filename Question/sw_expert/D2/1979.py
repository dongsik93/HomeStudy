T = int(input())

for tc in range(1,T+1):
    li = list(map(int,input().split()))
    n = li[0]
    k = li[1]

    table = []
    for oi in range(0,n):
        li2 = list(map(int, input().split()))
        table.append(li2)
        
        
    cnt = 0
    for y in range(0,n):
        sum = 0
        sumli = []
        for x in range(0,n):
            if table[y][x] == 0:
                sumli.append(sum)
                sum = 0
            elif table[y][x] == 1:
                sum +=1
        sumli.append(sum)
        for c in sumli:
            if c == k:
                cnt +=1
    cnty = 0

    for y in range(0,n):
        sum = 0
        sumli = []
        for x in range(0,n):
            if table[x][y] == 0:
                sumli.append(sum)
                sum = 0
            elif table[x][y] == 1:
                sum += 1
        sumli.append(sum)
        for c in sumli:
            if c == k:
                cnty +=1

    res = cnt + cnty
    print(f'#{tc} {res}')