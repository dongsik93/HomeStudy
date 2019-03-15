di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(farm, i, j,n, m):
    farm[i][j] = 0
    q = []
    q.append(i)
    q.append(j)
    while(len(q) > 0):
        x = q.pop(0)
        y = q.pop(0)
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if(0 <= dx and dx < n and 0 <= dy and dy < m):
                if(farm[dx][dy] == 1):
                    farm[dx][dy] = 0
                    q.append(dx)
                    q.append(dy)
    return


T = int(input())

for tc in range(T):
    m, n, k = map(int, input().split())

    farm = [[0]*m for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if(farm[i][j] == 1):
                bfs(farm, i, j, n, m)
                cnt += 1
    print(cnt)
