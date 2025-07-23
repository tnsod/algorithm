import sys
def input():return sys.stdin.readline().rstrip()

T=int(input())
for _ in range(T):
    n=int(input())
    arr=[(int(input()),i) for i in range(1,n+1)]
    m=max(arr)
    c=0
    for i in arr:
        if i[0]==m[0]: c+=1
    s=sum([i[0] for i in arr])
    if c>1: print("no winner")
    elif m[0]>s/2: print(f"majority winner {m[1]}")
    else: print(f"minority winner {m[1]}")
