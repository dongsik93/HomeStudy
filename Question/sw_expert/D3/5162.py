T = int(input())

for tc in range(T):
    a, b, c = map(int, input().split())
    count = []
    count.append(c // a)
    count.append(c // b)
    count.append(c // (a % c + b))
    count.sort()
    print("#{} {}".format(tc+1, max(count)))