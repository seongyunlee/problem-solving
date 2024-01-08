import heapq
n,*i=open(0).read().split()
q=[]
o=[]
for a in i:
    a=int(a)
    if a==0:
        o.append(0 if not q else heapq.heappop(q))
    else:
        heapq.heappush(q,a)
print(*o,sep="\n")