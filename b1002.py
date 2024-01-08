import math
for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    if(x1==x2 and y1==y2 and r1 ==r2):
        print(-1)
        continue
    dis=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if(abs(r1+r2-dis)<0.0000000001):
        print(1)
    elif(r1+r2<dis):
        print(0)
    elif(abs(abs(r1-r2)-dis)<0.000000001):print(1)
    elif(abs(r1-r2)<dis):
        print(2)
    elif(abs(r1-r2)>dis):print(0)