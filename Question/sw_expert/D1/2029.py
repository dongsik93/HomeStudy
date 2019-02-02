T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    for j in range(1):
        quot = a // b
        remain = a % b
    print(f"#{i+1} {quot} {remain}")
