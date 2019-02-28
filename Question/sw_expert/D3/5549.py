import sys

sys.stdin = open("input.txt", "r")

T = int(input())

res = []
for tc in range(T):
    n = input()
    if(int(n[-1]) % 2 == 0):
        res.append("Even")
    else:
        res.append("Odd")
for i in range(T):
    print(f"#{i+1} {res[i]}")