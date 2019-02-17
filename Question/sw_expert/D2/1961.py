T = int(input())

for i in range(T):
    N = int(input())

    arr = []
    for j in range(N):
        arr.append(list(map(int, input().split())))
    
    new_arr9 = []
    for j in range(len(arr)):
        for k in range(len(arr)-1,-1,-1):
            new_arr9.append(arr[k][j])
    
    
    new_arr18 = []
    for j in range(len(arr)-1,-1,-1):
        for k in range(len(arr)-1,-1,-1):
            new_arr18.append(arr[j][k])

    new_arr27 = []
    for j in range(len(arr)-1,-1,-1):
        for k in range(len(arr)):
            new_arr27.append(arr[k][j])

    arr9 = []
    for j in range(0,len(new_arr9),N):
        arr9.append(new_arr9[j:N+j])

    arr18 = []
    for j in range(0,len(new_arr18),N):
        arr18.append(new_arr18[j:N+j])

    arr27 = []
    for j in range(0,len(new_arr27),N):
        arr27.append(new_arr27[j:N+j])

    print(f"#{i+1}")
    
    for j in range(N):
        for k in range(N):
            print(arr9[j][k], end="")
        print(end=" ")
        for x in range(N):    
            print(arr18[j][x], end="")
        print(end=" ")
        for y in range(N):
            print(arr27[j][y], end="")
        print()
