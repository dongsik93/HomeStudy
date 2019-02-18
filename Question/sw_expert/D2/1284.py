T = int(input())

for tc in range(T):
    P, Q, R, S, W= map(int, input().split())

    A = W * P
    if(W <= R):
        B = Q
    else:
        B = (W - R) * S + Q
    
    res = 0
    if(A > B):
        res = B
    else:
        res = A

    print(f"#{tc+1} {res}")