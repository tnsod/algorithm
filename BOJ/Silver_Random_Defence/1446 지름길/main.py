import sys
input=sys.stdin.readline

road=[[] for _ in range(10001)]
dp=[int(1e9)]*10001
dp[0]=0
N,D=map(int,input().split())
for _ in range(N):
    a,b,c=map(int,input().split())
    road[a].append((b,c))

for i in range(10000):
    if road[i]:
        for b,c in road[i]:
            dp[b]=min(dp[b],dp[i]+c)
    dp[i+1]=min(dp[i+1],dp[i]+1)
print(dp[D])
