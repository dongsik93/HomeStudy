import collections
import sys

input = sys.stdin.readline
# 4방향 검사
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# bfs
def bfs(i, j, n, t):
    q = collections.deque() # 큐 생성
    q.append((i,j))
    visited[i][j] = 1
    while(q):
        x, y = q.popleft()
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if(0<=dx and dx<n and 0<=dy and dy<n):
                if(a[dx][dy] >= t and visited[dx][dy] == 0):
                    visited[dx][dy] = 1
                    q.append((dx,dy))

n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ans = []
rain = list(range(101))
# print(rain)
for t in rain:
    cnt = 0
    visited = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(visited[i][j] == 0 and a[i][j] >= t):
                bfs(i,j,n,t)
                cnt += 1
    ans.append(cnt)

# print(*visited, sep="\n")
print(max(ans))