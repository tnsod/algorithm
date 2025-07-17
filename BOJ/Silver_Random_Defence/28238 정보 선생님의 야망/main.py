import sys
input=sys.stdin.readline

n=int(input())
day=[[0]*5 for _ in range(4)]
student=[tuple(map(int,input().split())) for _ in range(n)]
for s in student:
    for i in range(4):
        for j in range(i+1,5):
            if s[i] and s[j]:
                day[i][j]+=1


max_v=0
idx_i,idx_j=0,0
for i in range(4):
    for j in range(5):
        if day[i][j]>max_v:
            idx_i=i
            idx_j=j
            max_v=day[i][j]

if idx_i==idx_j:
    print(0)
    print(1,1,0,0,0)
    exit()

ans=[0,0,0,0,0]
ans[idx_i]=1;ans[idx_j]=1
print(max_v)
print(*ans)
