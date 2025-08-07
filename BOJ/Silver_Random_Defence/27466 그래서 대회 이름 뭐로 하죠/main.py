import sys
def input():return sys.stdin.readline().rstrip()

vo={'A','E','I','O','U'}
N,M=map(int,input().split())
s=input()
ans=[]
flag=0
for i in range(N-1,-1,-1):
    if flag==0 and s[i] not in vo:
        ans+=s[i],
        flag=1
    elif flag==1 and s[i]=='A':
        ans+=s[i],
        flag=2
    elif flag==2 and s[i]=='A':
        ans+=s[i],
        flag=3
    elif flag==3:
        ans+=s[i],
    else:
        continue

while len(ans)>M:
    ans.pop()

if len(ans)==M:
    print('YES')
    print(*ans[::-1],sep='')
else:
    print('NO')
