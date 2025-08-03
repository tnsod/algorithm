import sys
input=sys.stdin.readline

N=int(input())
pair=[]
f=0
for i in range(N):
    n=int(input())
    pair+=n,
    f+=n*(-1)**i
f//=2

print(f)
for i in pair[:-1]:
    print(i-f)
    f=i-f
