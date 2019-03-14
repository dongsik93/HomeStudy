import sys
from collections import deque
input = sys.stdin.readline

di = [0,1,1]
dj = [1,0,1]


def bfs(i,j,n,s):
    q = deque()
    q.append((i,j))
    q.append(s)
    cnt = 0
    while(q):
        x, y = q.popleft()
        k = q.popleft()
        if(x== n-1 and y== n-1):
            cnt += 1
        if(k == 0): # 오른쪽
            dx = x + di[k]
            dy = y + dj[k]
            if(0<=dx and dx<n and 0<=dy and dy<n):
                if(arr[dx][dy] == 0):
                    q.append((dx,dy))
                    q.append(0)
            dx = x + di[2]
            dy = y + dj[2]
            if (0 <= dx and dx < n and 0 <= dy and dy < n):
                if (arr[dx-1][dy] == 0 and arr[dx][dy] == 0 and arr[dx][dy-1] == 0 ):
                    q.append((dx,dy))
                    q.append(2)
        elif(k == 1): # 아래쪽
            dx = x + di[k]
            dy = y + dj[k]
            if(0<=dx and dx<n and 0<=dy and dy<n):
                if(arr[dx][dy] == 0):
                    q.append((dx,dy))
                    q.append(1)
            dx = x + di[2]
            dy = y + dj[2]
            if (0 <= dx and dx < n and 0 <= dy and dy < n):
                if (arr[dx-1][dy] == 0 and arr[dx][dy] == 0 and arr[dx][dy-1] == 0):
                    q.append((dx,dy))
                    q.append(2)
        elif(k == 2): # 대각선
            dx = x + di[k]
            dy = y + dj[k]
            if (0 <= dx and dx < n and 0 <= dy and dy < n):
                if (arr[dx-1][dy] == 0 and arr[dx][dy] == 0 and arr[dx][dy-1] == 0):
                    q.append((dx, dy))
                    q.append(2)
            dx = x + di[1]
            dy = y + dj[1]
            if (0 <= dx and dx < n and 0 <= dy and dy < n):
                if (arr[dx][dy] == 0):
                    q.append((dx, dy))
                    q.append(1)
            dx = x + di[0]
            dy = y + dj[0]
            if (0 <= dx and dx < n and 0 <= dy and dy < n):
                if (arr[dx][dy] == 0):
                    q.append((dx, dy))
                    q.append(0)
    return cnt




n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
visited=[[0]*n for i in range(n)]
print(bfs(0,1,n,0))
