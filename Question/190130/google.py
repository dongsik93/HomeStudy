def num_count(num):
    num = str(num)
    return num.count("8")

sum = 0

for i in range(1,10000):
    sum += num_count(i)

print(sum)