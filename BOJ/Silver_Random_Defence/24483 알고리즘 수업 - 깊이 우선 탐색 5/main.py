import io,os
import sys
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.setrecursionlimit(int(1e9))

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for l in graph:
    l.sort()

depth=[0]*(N+1)
rank=[0]*(N+1)
cnt=0
def dfs(x):
    global cnt
    cnt+=1
    rank[x]=cnt
    visited[x]=True
    for nxt in graph[x]:
        if not visited[nxt]:
            depth[nxt]=depth[x]+1
            dfs(nxt)

dfs(R)
print(sum([depth[i]*rank[i] for i in range(1,N+1)]))
