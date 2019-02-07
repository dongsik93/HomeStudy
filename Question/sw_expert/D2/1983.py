def grade(num, rank):
    import math
    n = math.ceil(rank / (num / 10))
    if(n == 1):
        return "A+"
    elif(n == 2):
        return "A0"
    elif(n == 3):
        return "A-"
    elif(n == 4):
        return "B+"
    elif(n == 5):
        return "B0"
    elif(n == 6):
        return "B-"
    elif(n == 7):
        return "C+"
    elif(n == 8):
        return "C0"
    elif(n == 9):
        return "C-"
    else:
        return "D0"


T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    score = []
    for idx, j in enumerate(range(N),1):
        mid, fin, proj = map(int, input().split())
        total = mid * 0.35 + fin * 0.45 + proj * 0.2
        score.append([total,idx])
    score.sort(reverse=True)
    for j in range(len(score)):
        if(score[j][1] == K):
            print(f"#{i+1} {grade(N,j+1)}")
            
    