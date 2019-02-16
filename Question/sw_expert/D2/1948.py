T = int(input())

cal = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
    7:31, 8:31, 9:30, 10:31, 11:30, 12:31
    }


for i in range(T):
    a = list(map(int, input().split()))
    if(a[0] == a[2]):
        res = a[3] - a[1]
    else:
        x = a[0]
        res = 0
        while(x!=(a[2]-1)):
            x += 1 
            res += cal[x] 
        
        res = res + cal[a[0]]-a[1] + a[3]
    print("#"+str(i+1)+" "+str(res+1))

