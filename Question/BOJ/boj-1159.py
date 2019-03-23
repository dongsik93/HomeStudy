n = int(input())

team = []
for i in range(n):
    team.append(list(input()))

first = []
for i in team:
    if(i[0] not in first):
        first.append(i[0])
        
res = []
for k in range(len(first)):
    cnt = 0
    for i in range(n):
        for j in range(1):
            if(team[i][j] == first[k]):
                cnt += 1
    if(cnt >= 5):
        res.append(first[k])

if(res):
    print(*sorted(res),sep="")
else:
    print("PREDAJA")


