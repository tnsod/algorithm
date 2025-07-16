from collections import deque
import sys
def input():return sys.stdin.readline().rstrip()

Q=int(input())
q=deque()
flag=0 #0: 뒤 앞, 1: 뒤/앞, 2: 앞 뒤, 3: 앞/뒤
cnt_w=0
for _ in range(Q):
    c=input().split()
    if c[0]=='pop':
        if not q: continue
        elif flag==0 or flag==2 or flag==3:
            n=q.pop()
            if n=='w':cnt_w-=1
        else: 
            q.pop();cnt_w-=1
            while q and q[-1]!='w': q.pop()

    else:
        a,b=c[0],c[1]
        
        if a=='push':
            if b=='w': cnt_w+=1
            elif b=='b' and flag==3: continue
            elif b=='b' and flag==1 and not cnt_w: continue
            q.appendleft(b)
        
        elif a=='rotate':
            if b=='r':
                if flag==0:
                    flag=1
                    while q and q[-1]!='w':
                        q.pop()
                elif flag==1:
                    flag=2
                elif flag==2:
                    flag=3
                    while q and q[0]!='w':
                        q.popleft()
                else:
                    flag=0
            else:
                if flag==0:
                    flag=3
                    while q and q[0]!='w':
                        q.popleft()
                elif flag==1:
                    flag=0
                elif flag==2:
                    flag=1
                    while q and q[-1]!='w':
                        q.pop()
                else:
                    flag=2
        
        else:
            print(len(q)-cnt_w if b=='b' else cnt_w)
