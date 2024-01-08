def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
s=[]
from sys import stdin
for i in range(int(input())):
    s.append(list(map(int,stdin.readline().split())))
s.sort(key=lambda x:x[-1])
now=0
for i in range(len(s)):
    cnt=1
    for j in range(i+1,len(s)):
        x1,y1,x2,y2,w12=s[i]
        x3,y3,x4,y4,w34=s[j]
        if not (ccw(x1,y1,x2,y2,x3,y3) *ccw(x1,y1,x2,y2,x4,y4)>0 or ccw(x3,y3,x4,y4,x1,y1)* ccw(x3,y3,x4,y4,x2,y2)>0):
            cnt+=1
    now+=cnt*s[i][-1]
print(now)
