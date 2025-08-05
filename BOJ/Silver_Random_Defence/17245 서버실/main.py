import io,os
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def solve(computer):
    max_cnt=0
    for row in computer:
        m=max(row)
        if m>max_cnt:
            max_cnt=m
    half=0
    floor=[0]*(max_cnt+1)
    for row in computer:
        half+=sum(row)
        for cnt in row:
            floor[cnt]+=1
    half/=2

    dp=[0]*(max_cnt+2)
    for i in range(max_cnt,0,-1):
        dp[i]=dp[i+1]+floor[i]
    s=0
    for i in range(max_cnt+1):
        s+=dp[i]
        if s>=half:
            return i

def main():
    N=int(input())
    computer=[tuple(map(int,input().split())) for _ in range(N)]
    print(solve(computer))

if __name__=='__main__':
    main()
