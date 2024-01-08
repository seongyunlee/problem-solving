file=open('input.txt')
N,*lines=file.readlines()
import heapq
jewel=[list(map(int,x.split())) for x in lines[:int(N.split()[0])]]
bag=[int(x.strip()) for x in lines[int(N.split()[0]):]]
bag.sort()
jewel.sort(key=lambda x:x[0])
q=[]
value=0
idx=0
for b in bag:
    while idx<len(jewel) and jewel[idx][0]<=b:
        heapq.heappush(q,-jewel[idx][1])
        idx+=1
    if q:value-=heapq.heappop(q)
print(value)