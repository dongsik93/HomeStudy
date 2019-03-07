import sys
import collections
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(n, m):
    while(len(q) != 0):
        x = q.popleft()
        y = q.popleft()
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if(0<= dx and dx < n and 0 <= dy and dy < m):
                if(pot[dx][dy] == 0 and visited[dx][dy] == 0):
                    visited[dx][dy] = visited[x][y] + 1
                    q.append(dx)
                    q.append(dy)
    return visited

m, n = map(int, input().split())

pot = []
for i in range(n):
    pot.append(list(map(int, input().split())))

q = collections.deque([])
visited = [[0]*m for i in range(n)]
# q =[]
for i in range(n):
    for j in range(m):
        if(pot[i][j] == 1):
            q.append(i)
            q.append(j)
            visited[i][j] = 1
        elif(pot[i][j] == -1):
            visited[i][j] = -1
a = bfs(n,m)

res = 0
s = 0
for i in a:
    if(s < max(i)):
        s = max(i)

if(s == 1):
    res = 0
else:
    res = s -1

for i in a:
    if(0 in i):
        res = -1

print(res)