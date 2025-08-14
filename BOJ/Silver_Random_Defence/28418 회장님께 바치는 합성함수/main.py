a,b,c=map(int,input().split())
d,e=map(int,input().split())
p1,p2,p3=a*d*d,a*2*d*e+b*d,a*e*e+b*e+c
q1,q2,q3=d*a,d*b,d*c+e
x,y,z=p1-q1,p2-q2,p3-q3
if x==0:
    if y!=0:
        print("Remember my character")
    elif z==0:
        print("Nice")
    else:
        print("Head on")
else:
    t=y*y-4*x*z
    if t>0:
        print("Go ahead")
    elif t==0:
        print("Remember my character")
    else:
        print("Head on")
