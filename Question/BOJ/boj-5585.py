n = int(input())

coin = [1,5,10,50,100,500]

n = 1000 - n

cnt = 0
while(n != 0):
    if(n>=500):
        cnt += n//500
        n = n % 500
    elif(n>=100):
        cnt += n//100
        n = n % 100
    elif(n>=50):
        cnt += n//50
        n = n % 50
    elif(n>=10):
        cnt += n//10
        n = n % 10
    elif(n>=5):
        cnt += n//5
        n = n % 5
    else:
        cnt += n
        n = 0

print(cnt)