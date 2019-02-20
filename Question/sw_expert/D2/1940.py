import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())
    ms = 0
    distance = 0
    for i in range(n):
        command = []
        command.append(list(map(int, input().split())))
        for j in range(1,len(command)+1):
            if(command[0][j-1] == 1):
                ms += command[0][j]
                distance += ms
            elif(command[0][j-1] == 2):
                if(ms < command[0][j]):
                    ms = 0
                else:
                    ms -= command[0][j]
                    distance += ms
            else:
                distance += ms

    print(f"#{tc+1} {distance}")