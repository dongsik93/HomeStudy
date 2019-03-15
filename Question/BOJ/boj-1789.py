n = int(input())

cnt = 0
sums = 0
i = 1
while(n >= sums):
    sums += i
    cnt += 1
    i += 1

if(n < sums):
    cnt -= 1

print(cnt)