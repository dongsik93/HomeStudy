import sys

sys.stdin = open('input.txt', 'r', encoding='UTF8')


for tc in range(10):
    T = int(input())
    find = input()
    word = input()

    cnt = 0
    for i in range(1,len(word)):
        if(word[i-1] == find[0]):
            if(word[i:i+len(find)-1] == find[1:]):
                cnt += 1
    
    print(f"#{tc+1} {cnt}")