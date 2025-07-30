N=int(input())
s=input()
cnt=0
for i in range(1,N):
    if s[i-1]==']' and s[i]=='[':
        continue
    elif s[i-1]=='5' and s[i]=='5':
        cnt+=2
    elif s[i-1]=='2' and s[i]=='2':
        cnt+=2
    else:
        cnt+=1
print(cnt)
