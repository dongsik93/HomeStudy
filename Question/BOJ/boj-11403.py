import sys

input = sys.stdin.readline

di = [0,1,0,-1]
dj = [1,0,-1,0]


def bfs(i,j,n):
    q = []
    q.append((i,j))
    visited[i][j] = 1
    while(q):
        x, y = q.pop(0)
        for i in range(4):
            dx = x + di[i]
            dy = y + dj[i]
            if(0<=dx and dx<n and 0<=dy and dy<n):
                if(visited[])

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


visited = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if(arr[i][j] == 1 and visited[i][j] == 0):
            bfs(i,j,n)
