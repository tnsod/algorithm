import sys
input=sys.stdin.readline

N=int(input())
P,T=map(int,input().split())
cycle=T//(4*N-2)
n=T%(4*N-2)
hands=((2*N*(2*N+1))//2)*cycle+(2*N*(2*N+1)//2-1-2*N)*cycle
tmp=None
if n>2*N:
    hands+=2*N*(2*N+1)//2
    tmp=2*N-1
    n=n-2*N-1
    while n>0:
        hands+=tmp
        tmp-=1
        n-=1
else:
    tmp=1
    n-=1
    while n>0:
        hands+=tmp
        tmp+=1
        n-=1

now=hands%(N*2)
pos=P*2-1
if now<=pos<=now+tmp or now<=pos+N*2<=now+tmp:
    print("Dehet YeonJwaJe ^~^")
else:
    print("Hing...NoJam")
