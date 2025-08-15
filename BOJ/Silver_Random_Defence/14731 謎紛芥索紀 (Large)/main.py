import sys
input=sys.stdin.readline
MOD=int(1e9)+7

def pow(a,n):
    if n==-1: return 0
    if n==0: return 1

    x=pow(a,n//2)
    if n%2:
        return x*x*a%MOD
    else:
        return x*x%MOD

N=int(input())
ans=0
for _ in range(N):
    a,b=map(int,input().split())
    ans+=a*b*pow(2,b-1)%MOD
print(ans%MOD)
