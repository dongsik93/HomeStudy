T = int(input())

for i in range(T):
    word = input()
    my_word = []
    min = word.count(word[0]) 
    for j in range(len(word)):
        if(word[j] not in my_word):
            my_word.append(word[j]) 
        if(word.count(word[j]) < min ): 
            min = word.count(word[j])

    answer = []
    for k in range(len(my_word)):
        a = (word.count(my_word[k]) // min) * my_word[k]
        answer.append(a)
    answer = "".join(answer)
    print(f"#{i+1} {len(answer)}")