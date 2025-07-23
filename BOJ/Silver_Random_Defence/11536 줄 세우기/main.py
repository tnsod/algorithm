import sys
def input():return sys.stdin.readline().rstrip()

N=int(input())
name=[input() for _ in range(N)]
i_name=sorted(name)
d_name=sorted(name,reverse=True)
if name==i_name: print("INCREASING")
elif name==d_name: print("DECREASING")
else: print("NEITHER")
