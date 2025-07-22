import sys
def input():return sys.stdin.readline().rstrip()

dic={}
N=int(input())
for _ in range(N):
    s=input()
    dic[(s[0]+s[-1],''.join(sorted(s)))]=s

input()
S=input().split()
for i in S:
    print(dic[(i[0]+i[-1],''.join(sorted(i)))],end=' ')
