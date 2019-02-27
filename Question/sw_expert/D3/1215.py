import sys

sys.stdin = open("input.txt", "r")

for tc in range(10):
    arr = []
    n = int(input())
    for i in range(8):
        arr.append(list(input()))
    
    arr_col = []        
    for i in range(8):
        plus = []
        for j in range(8-1, -1, -1):
            plus.append(arr[j][i])
        arr_col.append(plus)

    cnt_col = 0
    cnt_row = 0
    for i in range(8):
        for j in range(n+1):
            if(arr[i][j:j+n-1] == arr[i][j+n-1:j:-1]):
                cnt_row += 1
            if(arr_col[i][j:j+n-1] == arr_col[i][j+n-1:j:-1]):
                cnt_col += 1

    print(f"#{tc+1} {cnt_row + cnt_col}")