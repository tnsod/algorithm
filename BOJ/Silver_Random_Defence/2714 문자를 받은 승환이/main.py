import sys
def input():return sys.stdin.readline().rstrip()

def make_graph(R,C,message):
    graph=[]
    for i in range(R):
        row=message[i*C:(i+1)*C]
        graph.append(row)
    return graph

def circuit(R,C,graph):
    visited=[[False]*C for _ in range(R)]
    flag=0 #0:오른쪽, 1:아래, 2:왼쪽, 3:위
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    y=x=0
    res=[]
    tmp=''
    for i in range(R*C):
        tmp+=graph[y][x]
        visited[y][x]=True
        if len(tmp)==5:
            res.append(tmp)
            tmp=''
        if i==R*C-1: break

        ny=y+direction[flag][1]
        nx=x+direction[flag][0]
        while not (0<=ny<R and 0<=nx<C and not visited[ny][nx]):
            flag=(flag+1)%4
            ny=y+direction[flag][1]
            nx=x+direction[flag][0]
        y,x=ny,nx
    
    return res

def main():
    T=int(input())
    for _ in range(T):
        R,C,message=input().split()
        R,C=map(int,(R,C))
        graph=make_graph(R,C,message)
        res=circuit(R,C,graph)
        ans=''
        for bin in res:
            n=int(bin,2)
            ans+=' ' if n==0 else chr(64+n)
        print(ans.rstrip())

if __name__=='__main__':
    main()
