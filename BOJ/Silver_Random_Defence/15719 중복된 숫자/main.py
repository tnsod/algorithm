import os
def generator():
    d_iter=os.read(0, os.fstat(0).st_size)
    tmp=bytearray()
    for i in d_iter:
        if i in b' \n':
            yield int(tmp.decode())
            tmp.clear()
        else:
            tmp.append(i)

def main():
    g=generator()
    N=next(g)
    sum=0
    s=((N-1)*N)//2
    for _ in range(N):
        n=next(g)
        sum+=n
    print(sum-s)

if __name__=='__main__':
    main()
