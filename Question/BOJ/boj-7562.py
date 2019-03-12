di = [1, 2, 2, 1, -1, -2, -2,-1]
dj = [2, 1, -1,-2,-2, -1, 1,2]

def bfs(i, j , xx, yy, n):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    cnt = 0
    while(q):
        size = len(q)
        for i in range(size):
            x, y = q.pop(0)
            if(x == xx and y == yy):
                return cnt
            for k in range(8):
                dx = x + di[k]
                dy = y + dj[k]
                if(0<=dx and dx<n and 0<=dy and dy<n):
                    if(visited[dx][dy] == 0):
                        q.append((dx,dy))
                        visited[dx][dy] = 1
        cnt += 1
    return 0

T = int(input())
res = []
for tc in range(T):
    n = int(input())
    i, j = map(int, input().split())
    x, y = map(int, input().split())
    visited = [[0]*n for i in range(n)]
    res.append(bfs(i, j, x, y, n))

print(*res, sep="\n")