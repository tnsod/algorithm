import sys
input=sys.stdin.readline

N,M,K,X,Y=map(int,input().split())
m=[]
for i in range(N):
    A,B=map(int,input().split())
    m.append(A*X-B*Y)
m.sort()

ans=K*(X+Y)
for i in range(M):
    ans+=m[i]
print(ans)
