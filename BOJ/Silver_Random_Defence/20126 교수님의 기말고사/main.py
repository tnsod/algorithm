import sys
input=sys.stdin.readline

N,M,S=map(int,input().split())
time=[tuple(map(int,input().split())) for _ in range(N)]
time.sort()

if M<=time[0][0]:
    print(0)
    exit()

for i in range(N-1):
    st=time[i][0]
    en=st+time[i][1]
    if M<=time[i+1][0]-en:
        print(en)
        exit()

if M<=S-(time[-1][0]+time[-1][1]):
    print(time[-1][0]+time[-1][1])
    exit()

print(-1)
