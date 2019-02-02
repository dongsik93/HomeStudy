def d(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum+int(n)

a = []
for i in range(1,5000):
    if(d(i) not in a):
        a.append(d(i))

sum = 0
for i in range(1,5000):
    if(i not in a):
        sum += i 

print(sum)
