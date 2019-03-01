T = int(input())

for tc in range(T):
    mem = list(input())

    bit = list(len(mem)*"0")

    cnt = 0

    for i in range(len(mem)):
        if(mem[i] != bit[i]):
            for j in range(i,len(mem)):
                bit[j] = mem[i]
            cnt += 1
    print(f"#{tc+1} {cnt}")