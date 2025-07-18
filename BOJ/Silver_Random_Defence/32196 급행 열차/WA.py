import heapq
import sys
input=sys.stdin.readline

N,M,K,X,Y=map(int,input().split())
q=[]
heapq.heapify(q)
for i in range(N):
    A,B=map(int,input().split())
    heapq.heappush(q,(A-B,A,B))

ans=K*X+K*Y
for _ in range(M):
    n=heapq.heappop(q)
    ans+=n[1]*X
    ans-=n[2]*Y
print(ans)
