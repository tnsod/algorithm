import sys
input=sys.stdin.readline

N,K=map(int,input().split())
m=1
for _ in range(K):
    m*=N
    N-=1

n=1
for i in range(2,K+1):
    n*=i
print((m//n)%10007)
