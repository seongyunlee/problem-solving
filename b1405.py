import copy
n,E,W,S,N = map(int,input().split())
E,W,S,N=[x/100 for x in [E,W,S,N]]
bfs=[[0,0,1]]
odd=1.00
count=0
visit=[[False]*(2*n+1) for _ in range(2*n+1)]
visit[n][n]=True
while bfs and count<n:
    next_bfs=[]
    new_visit=copy.deepcopy(visit)
    count=count+1
    for b in bfs:
        east,north,now_odd =b
        if visit[east+1+n][north+n]:
            odd=odd-now_odd*E
        else:
            next_bfs.append([east+1,north,now_odd*E])
            new_visit[east+1+n][north+n]=True
        if visit[east-1+n][north+n]:
            odd=odd-now_odd*W
        else:
            next_bfs.append([east-1,north,now_odd*W])
            new_visit[east-1+n][north+n]=True
        if visit[east+n][north-1+n]:
            odd=odd-now_odd*S
        else:
            next_bfs.append([east,north-1,now_odd*S])
            new_visit[east+n][north-1+n]=True
        if visit[east+n][north+1+n]:
            odd=odd-now_odd*N
        else:
            next_bfs.append([east,north+1,now_odd*N])
            new_visit[east+n][north+1+n]=True
    bfs=next_bfs
    visit=new_visit
    print(str(count)+":"+str(odd))
    print(str(count)+":"+str(bfs))
print(odd)
