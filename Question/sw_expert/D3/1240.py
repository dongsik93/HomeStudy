import sys

sys.stdin = open("input.txt", "r")


code = {
    0:[1,0,1,1,0,0,0],
    1:[1,0,0,1,1,0,0],
    2:[1,1,0,0,1,0,0],
    3:[1,0,1,1,1,1,0],
    4:[1,1,0,0,0,1,0],
    5:[1,0,0,0,1,1,0],
    6:[1,1,1,1,0,1,0],
    7:[1,1,0,1,1,1,0],
    8:[1,1,1,0,1,1,0],
    9:[1,1,0,1,0,0,0]
}


aa = []
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())

    arr = []
    for i in range(n):
        a = list(map(int,input()))
        arr.append(a)

    res = []
    for i in range(n):
        for j in range(m-1,-1,-1):
            if(arr[i][j] == 1):
                res.append(arr[i][j:j-56:-1])
                break
    ret = 0
    # print(*res, sep="\n")
    for i in range(len(res)):
        s = []
        for j in range(0,len(res[i]),7):
            for k in range(10):
                # print(i,j,k)
                if(res[i][j:j+7] == code[k]):
                    s.append(k)
        s = s[::-1]
        ssum = 0
        tsum = 0
        for j in range(8):
            if(j%2 == 0):
                ssum += s[j]
            else:
                tsum += s[j]
        if((ssum*3 + tsum) % 10 == 0):
            ret = sum(s)
        else:
            ret = 0
            break
    aa.append(ret)
for i in range(T):
    print("#{} {}".format(i+1, aa[i]))
# print(*aa, spe="\n")
#     print("#{} {}".format(tc+1, ret))

