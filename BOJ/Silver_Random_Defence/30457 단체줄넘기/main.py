input()
A=tuple(map(int,input().split()))
dic={}
for i in A:
    dic[i]=dic.get(i,0)+1
ans=0
for j in dic:
    if dic[j]==1:
        ans+=1
    else:
        ans+=2
print(ans)
