import sys
def input():return sys.stdin.readline().rstrip()

t=int(input())
M=int(input())
graph=[[] for _ in range(4)]
for _ in range(M):
    s,e,d=input().split()
    s,e=map(lambda x:ord(x)-65,(s,e))
    graph[s].append((e,float(d)))

per=[25,25,25,25]
for _ in range(t):
    t_per=[0,0,0,0]
    for i in range(4):
        for j in graph[i]:
            t_per[j[0]]+=per[i]*j[1]
    per=t_per

for i in per:
    print(format(i,'.2f'))
