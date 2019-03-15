a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = p * a
if(p <= c):
    y = b
else:
    y = b + (p-c)*d

print(min(x,y))