di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j, n, k):
    q = []
    q.append((i,j))
    visited[i][j] = 1
    while(q):
        x, y = q.pop(0)
        for i in range(4):
            dx = x + di[i]
            dy = y + dj[i]
            if(0<= dx and dx < n and 0 <= dy and dy < n):
                if(a[dx][dy] == k and visited[dx][dy] == 0):
                    visited[dx][dy] = 1
                    q.append((dx,dy))
    return 1

def bfs2(i, j, n, k, l):
    q = []
    q.append((i,j))
    visited2[i][j] = 1
    while(q):
        x, y = q.pop(0)
        for i in range(4):
            dx = x + di[i]
            dy = y + dj[i]
            if(0<= dx and dx < n and 0 <= dy and dy < n and visited2[dx][dy] == 0):
                if(a[dx][dy] == k or a[dx][dy] == l):
                    visited2[dx][dy] = 1
                    q.append((dx,dy))
    return 1


n = int(input())

a = []
for i in range(n):
    a.append(list(input()))

visited = [[0]*n for t in range(n)]
visited2 = [[0]*n for t in range(n)]

r = []
g = []
b = []
rg = []
for i in range(n):
    for j in range(n):
        if(a[i][j] == "R" and visited[i][j] == 0):
            r.append(bfs(i,j,n,a[i][j]))
        elif(a[i][j] == "G" and visited[i][j] == 0 ):
            g.append(bfs(i,j,n,a[i][j]))
        elif(a[i][j] == "B" and visited[i][j] == 0):
            b.append(bfs(i,j,n,a[i][j]))
        if(visited2[i][j] == 0):
            if(a[i][j] == "R" or a[i][j] == "G"):
                rg.append(bfs2(i, j, n, "R","G"))

rgb = len(r) + len(g) + len(b)
r_gb = len(rg) + len(b)
print(rgb, r_gb)