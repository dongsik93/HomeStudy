di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(apart, i, j, cnt):
    apart[i][j] = 0
    q = []
    q.append(i)
    q.append(j)

    while(len(q) > 0):
        x = q.pop(0)
        y = q.pop(0)
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if(0 <= dx and dx < n and 0 <= dy and dy < n):
                if(apart[dx][dy] == 1):
                    cnt += 1
                    apart[dx][dy] = 0
                    q.append(dx)
                    q.append(dy)
    return cnt

n = int(input())

apart = []
for i in range(n):
    apart.append(list(map(int, input())))

cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if(apart[i][j] == 1):
            res.append(bfs(apart, i, j, cnt+1))


print(len(res))
for i in sorted(res):
    print(i)
