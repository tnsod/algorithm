import sys
input=sys.stdin.readline

N,M=map(int,input().split())
price=[int(input()) for _ in range(M)]
price.sort()
cnt=M
ans1=0
ans2=0
for i in price:
    m=min(cnt,N)
    if ans2<i*m:
        ans2=i*m
        ans1=i
    cnt-=1
print(ans1,ans2)
