from queue import heappush,heappop
def solution(n, start, end, roads, traps):
    global dp,END,edges,T
    T={v:k for k,v in enumerate(traps)}
    print(T)
    edges={i:[] for i in range(1,n+1)}
    for f,t,c in roads:
        if f in T or t in T:
            edges[f].append([t,c,0])
            edges[t].append([f,c,1])
        else:
            edges[f].append([t,c,-1])
    hq=[(0,start,0)]
    visit=[[False]*(2**len(traps)) for _ in range(n+1)]
    print(edges)
    while hq:
        print(hq,visit)
        cost,node,mask=heappop(hq)
        if node==end:return cost
        if visit[node][mask]:continue
        visit[node][mask]=True
        if T.get(node)!=None:
            mask=mask^(2**T[node])
        bits=bin(mask)[2:].zfill(len(T))[::-1]
        for to,co,typ in edges[node]:
            if T.get(node)!=None and T.get(to)!=None:
                if int(bits[T[node]])^int(bits[T[to]])!=typ:continue
            elif T.get(node)!=None:
                if int(bits[T[node]])!=typ:continue
            elif T.get(to)!=None:
                if int(bits[T[to]])!=typ:continue
            heappush(hq,(cost+co,to,mask))
    return -1
#print(solution(3	,1,	3	,[[1, 2, 2], [3, 2, 3]]	,[2]))
print(solution(4	,1	,4	,[[1, 2, 1], [3, 2, 1], [2, 4, 1]]	,[2, 3]))