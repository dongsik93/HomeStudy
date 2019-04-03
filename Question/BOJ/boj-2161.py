from collections import deque

n = int(input())

card = deque(range(1,n+1))
arr = []

while(card):
    arr.append(card.popleft())
    card.rotate(-1)
print(*arr, sep=" ")