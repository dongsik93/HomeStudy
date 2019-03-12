import sys

input = sys.stdin.readline

def setmenu(x,y):
    return x+y-50


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(min(setmenu(a,d), setmenu(a,e),setmenu(b,d), setmenu(b,e), setmenu(c,d), setmenu(c,e),))
