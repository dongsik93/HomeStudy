T = int(input())

for i in range(T):
    word = input()
    ans = 1

    for j in range(len(word)):
        if(word[j] == word[-(j+1)]):
            ans = 1
        else:
            ans = 0
    print(f"#{i+1} {ans}")