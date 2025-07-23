import sys
input=sys.stdin.readline

def pow_two(n):
    i=1
    while i<n:
        i<<=1
    return i

while 1:
    G,T,A,D=map(int,input().split())
    if G==A==T==D==-1: break

    t=(T*(T-1))//2
    p=pow_two(G*A+D)
    X=G*t+p-1
    Y=p-(G*A+D)
    print(f'{G}*{A}/{T}+{D}={X}+{Y}')
