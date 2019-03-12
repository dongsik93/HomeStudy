di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j, n, m):
    q=[]
    q.append((i,j))
    cnt = 1
    maze[i][j] = 0
    while(q):
        size = len(q)
        for i in range(size):
            cx,cy = q.pop(0)
            if(cx==n-1 and cy == m-1):
                return cnt
            for j in range(4):
                nx = cx + di[j]
                ny = cy + dj[j]
                if(nx>=0 and ny>=0 and nx<n and ny<m):
                    if(maze[nx][ny]==1):
                        q.append((nx,ny))
                        maze[nx][ny] = 0
                        # visited[nx][ny]=1
        cnt+=1

n, m = map(int, input().split())

maze = []
visited=[[0]*m for x in range(n)]
for i in range(n):
    maze.append(list(map(int, input())))

res = bfs(0,0,n,m)

print(res)