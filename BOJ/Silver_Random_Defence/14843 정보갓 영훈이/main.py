import sys
input=sys.stdin.readline

N=int(input())
total=0
for _ in range(N):
    S,A,T,M=map(float,input().split())
    score=(S*(1+1/A)*(1+M/T))/4
    total+=score

P=int(input())
rank=[float(input()) for _ in range(P)]
rank+=total,
rank.sort(reverse=True)
x=0
for i in range(len(rank)):
    if rank[i]==total:
        x=i+1
        break

name='Younghoon "The God"' if x/len(rank)<=15/100 else 'Younghoon'
print(f'The total score of {name} is {total:.2f}.')
