T = int(input())
word = ["a", "e", "i", "o", "u"]
for tc in range(T):
    text = input()
    a = []
    for i in text:
        if(i not in word):
            a.append(i)
    a = "".join(a)
    print("{} {}".format(tc+1, a))