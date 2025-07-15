import sys
input=sys.stdin.readline

def lower_bound(arr,st,en,key):
    while st<en:
        mid=(st+en)//2
        if arr[mid]<key:
            st=mid+1
        else:
            en=mid
    return en
    
N=int(input())
arr=tuple(map(int,input().split()))
lis=[arr[0]]
for i in range(1,N):
    if lis[-1]<arr[i]:
        lis.append(arr[i])
    else:
        idx=lower_bound(lis,0,len(lis)-1,arr[i])
        lis[idx]=arr[i]

print(N-len(lis))
