T = int(input())

for tc in range(T):
    d, a, b, f = map(int, input().split())

    res = d/(a+b)*f
    print(f"#{tc+1} {res}")