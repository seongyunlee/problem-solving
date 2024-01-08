from itertools import combinations
from math import sqrt
file=open('input.txt')
T,*lines=file.readlines()
for _ in range(int(T)):
    pos=[]
    N=int(lines.pop(0))
    for _ in range(N):
        pos.append(list(map(int,lines.pop(0).split())))
    combi=list(combinations(list(range(0,len(pos))),len(pos)//2))
    dis=9999999999999999999999999999999
    for c in combi[:len(combi)//2+1]:
        sum_x=0
        sum_y=0
        for idx,p in enumerate(pos):
            minus=-1 if (idx in c)==True else 1
            sum_x+=minus*p[0]
            sum_y+=minus*p[1]
        dis=min(dis,sqrt(sum_x**2+sum_y**2))
    print(dis)
    