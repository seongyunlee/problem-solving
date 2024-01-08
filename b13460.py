N,M=map(int,input().split())
B=[list(input()) for _ in range(N)]
bx=by=0
rx=ry=0
for x in range(N):
    for y in range(M):
        if B[x][y]=="B":
            bx=x
            by=y
            B[x][y]="."
        elif B[x][y]=="R":
            rx=x
            ry=y
            B[x][y]="."
pool=[[bx,by,rx,ry]]


def moveBlue(dx,dy,rx,ry,bx,by):
    while True:
        if B[bx+dx][by+dy]=="#" or (bx+dx==rx and by+dy==ry):return [bx,by]
        elif B[bx+dx][by+dy]=="O":
            return [-1,-1]
        if B[bx+dx][by+dy]==".":
            bx+=dx
            by+=dy
def moveRed(dx,dy,rx,ry,bx,by):
    while True:
        if B[rx+dx][ry+dy]=="#" or  (rx+dx==bx and ry+dy==by):return [rx,ry]
        elif B[rx+dx][ry+dy]=="O":
            return [-1,-1]
        elif B[rx+dx][ry+dy]==".":
            rx+=dx
            ry+=dy
def solve():
    global pool
    for answer in range(10):
        new_pool=[]
        for bx,by,rx,ry in pool:
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                if (dx>0 and bx>rx) or (dx<0 and bx<rx) or (dy>0 and by>ry) or (dy<0 and by<ry):
                    nbx,nby=moveBlue(dx,dy,rx,ry,bx,by)
                    if nbx==-1 and nby==-1:continue
                    nrx,nry=moveRed(dx,dy,rx,ry,nbx,nby)
                    if nrx==-1 and nry==-1:return answer
                    new_pool.append([nbx,nby,nrx,nry])
                else:
                    nrx,nry=moveRed(dx,dy,rx,ry,bx,by)
                    nbx,nby=moveBlue(dx,dy,nrx,nry,bx,by)
                    if nrx==-1 and nry==-1 and nbx!=-1 and nby!=-1:
                        return answer
                    new_pool.append([nbx,nby,nrx,nry])
        pool=new_pool
    return -2
                
print(solve()+1)