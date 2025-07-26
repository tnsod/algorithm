import sys
input=sys.stdin.readline

n,m=map(int,input().split())
h=1
ans=['U 1 -10000']
for _ in range(m):
    a=int(input())
    ans.append(f'U {a+1} {h}')
    ans.append('P')
    h+=1
print(len(ans))
print(*ans,sep='\n')
