N = int(input())
num = map(int, input().split())
my_num = []
for i in num:
    my_num.append(i)
my_num.sort()

dot = int(N/2)
print(my_num[dot])