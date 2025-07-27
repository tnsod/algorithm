import sys
input=sys.stdin.readline

N=int(input())
arr=[]
arr2=[]
table={}
for _ in range(N):
    c,s=map(int,input().split())
    arr.append([(c,s),s])
    arr2.append([(c,s),s])
    table[(c,s)]=s

arr2.sort(key=lambda x:x[1])
dp=sorted(arr,key=lambda x:x[1])
cnt=0
for i in range(1,N):
    if arr2[i][1]>arr2[i-1][1]:
        dp[i][1]+=dp[i-1][1]+table[dp[i-1][0]]*cnt
        cnt=0
    else:
        dp[i][1]=dp[i-1][1]
        cnt+=1

dic={}
duplicate={}
for i in dp:
    duplicate[i[0][0]]=duplicate.get(i[0][0],0)+table[i[0]]
    if i[0] in dic:
        continue
    else:
        dic[i[0]]=i[1]-duplicate[i[0][0]]

for i in arr:
    print(dic[i[0]])
