import sys
input = sys.stdin.readline

def dfs(index):
    if(index == m):
        for i in range(m):
            print(visited[i], end=" ")
        print()
        return
    else:
        for i in range(1,n+1):
            visited[index] = i
            dfs(index+1)

n, m = map(int, input().split())

visited = [0 for i in range(8)]
dfs(0)