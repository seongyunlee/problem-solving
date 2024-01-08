import heapq
I=open(0).readlines()[::-1]
for k in range(int(I.pop())):
    MAXQ=[]
    MINQ=[]
    removed=[]
    for i in range(int(I.pop())):
        M,N=I.pop().split()
        if M=="I":
            heapq.heappush(MAXQ,[-int(N),len(removed)])
            heapq.heappush(MINQ,[int(N),len(removed)])
            removed.append(False)
        else:
            if N=='-1':Q=MINQ
            else:Q=MAXQ
            while Q:
                _,idx=heapq.heappop(Q)
                if not removed[idx]:
                    removed[idx]=True
                    break
    min=None
    max=None
    while MINQ:
        a,idx=heapq.heappop(MINQ)
        if not removed[idx]:
            min=a
            break
    while MAXQ:
        a,idx=heapq.heappop(MAXQ)
        if not removed[idx]:
            max=a
            break
    if min!=None:print(-max,min)
    else:print("EMPTY")