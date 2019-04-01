def isprime(n,m):
  a = [False, False,] + [True]*(m-1)
  for i in range(2,len(a)):
      if a[i]:
          prime.append(i)
          for j in range(2*i, m+1, i):
              a[j] = False

n = int(input())
m = int(input())
prime = []
isprime(n,m)
s = 0
minV = 10000
print(prime)
for i in prime:
    if(i >= n):
        s += i
    if(n <= i < minV ):
        minV = i
if(minV == 10000):
    print(-1)
else:
    print(s)
    print(minV)


# def prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i is 0:
#             return False
#     return True
#
#
# n = int(input())
# m = int(input())
# arr = list(range(n,m+1))
# cnt = 0
# s = -1
# minV = 10000
# for i in arr:
#     if prime(i):
#         s += i
#         if(minV > i):
#             minV = i
#
# if(s == -1):
#     print(s)
# else:
#     print(s+1)
#     print(minV)