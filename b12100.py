N=int(input())
M=[list(map(int,input().split())) for _ in range(N)]
answer=2
def move(direction,org):
    global N,answer
    dir = -1 if -1 in direction else 1
    if direction[1]==0:
        lines=[list(line) for line in org]
    else:
        lines=[[org[i][k] for i in range(N)] for k in range(N)]
    for nth in range(N):
        for fr in range(1 if dir>0 else N-1,N if dir>0 else -1,dir):
            my=lines[fr][nth]
            lines[fr][nth]=0
            if my==0:continue
            prev=fr
            for to in range(fr-dir,-1 if dir>0 else N,-dir):
                if lines[to][nth]==0:
                    prev=to
                elif lines[to][nth]==my and lines[to][nth]>0 and my>0:
                    prev=to
                    my=-2*my
                    lines[to][nth]=0
                else:
                    break
            lines[prev][nth]=my
    if direction[1]==0:
        M=[[abs(lines[i][j]) for j in range(N)] for i in range(N)]
    else:
        M=[[abs(lines[j][i]) for j in range(N)] for i in range(N)]
    answer=max(max([max(line) for line in M]),answer)
    return M
pool=[M]

for _ in range(5):
    new_pool=[]
    for now in pool:
        for k in [[-1,0],[1,0],[0,1],[0,-1]]:
            new_pool.append(move(k,now))
    pool=new_pool
print(answer)
