l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

cnt = 0
for i in range(l):
    if(b-d*i <=0 and a-c*i <= 0):
        break
    else:
        cnt += 1
print(l-cnt)