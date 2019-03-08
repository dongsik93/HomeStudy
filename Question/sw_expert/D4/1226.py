from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    q = deque()
    q.append((i,j))
    # q.append(i)
    # q.append(j)
    maze[i][j] = 1
    while(len(q) != 0):
        x,y = q.popleft()
        # x = q.pop(0)
        # y = q.pop(0)
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if(0 <= dx and dx < 16 and 0 <= dy and dy < 16):
                if(maze[dx][dy] == 0):
                    q.append((dx,dy))
                    # q.append(dx)
                    # q.append(dy)
                    maze[dx][dy] = 1
                elif(maze[dx][dy] == 3):
                    return 1
    return 0

for i in range(10):
    n = int(input())

    maze = []
    for i in range(16):
        maze.append(list(map(int, input())))

    for i in range(16):
        for j in range(16):
            if(maze[i][j] == 2):
                res = bfs(i, j)
    print("#{} {}".format(n, res))