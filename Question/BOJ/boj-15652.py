import sys
input = sys.stdin.readline

def dfs(index):
    if(index == m):
        if(check(visited) == 1):
            for i in range(m):
                print(visited[i], end=" ")
            print()
        return
    else:
        for i in range(1,n+1):
            visited[index] = i
            dfs(index+1)

def check(answer):
    for i in range(m-1):
        if answer[i+1] < answer[i]:
            return 0
    return 1

n, m = map(int, input().split())

visited = [0 for i in range(8)]
dfs(0)

# import itertools,sys
# a, b = map(int, sys.stdin.readline().rstrip().split())
# for i in itertools.combinations_with_replacement(range(1, a+1), b):
# 	print(*i)