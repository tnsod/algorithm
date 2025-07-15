N,M=map(int,input().split())
B=sum(i.count('x') for i in (input() for _ in range(N)))

for S in range(B//11+1):
    t=B-11*S
    if t%9==0:
        print(S,t//9)
        break
