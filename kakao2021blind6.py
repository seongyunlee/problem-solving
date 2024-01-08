from copy import deepcopy
answer=1e8
def card_list(board):
    card=[]
    for r,row in enumerate(board):
        for c,col in enumerate(row):
            if not col==0:card.append([r,c])
    return card
def move_target(board,r,c,r2,c2):
    if r==r2 and c==c2:return 0
    visit=[[False]*4 for _ in range(4)]
    visit[r][c]=True
    bfs=[[r,c]]
    cnt=0
    dxdy=[[-1,0],[1,0],[0,1],[0,-1]]
    while bfs:
        next_bfs=[]
        for r1,c1 in bfs:
            for dx,dy in dxdy:
                if 0<=dx+r1<=3 and 0<=dy+c1<=3:
                    if not visit[dx+r1][dy+c1]:
                        next_bfs.append([dx+r1,dy+c1])
                        visit[dx+r1][dy+c1]=True
            for dx,dy in dxdy:
                gap=1
                while True:
                    if not (0<=r1+gap*dx<=3 and 0<=c1+gap*dy<=3):break
                    if board[r1+gap*dx][c1+gap*dy]!=0:
                        if visit[r1+gap*dx][c1+gap*dy]==False:
                            next_bfs.append([r1+gap*dx,c1+gap*dy])
                            visit[r1+gap*dx][c1+gap*dy]=True
                        break
                    elif (dx==0 and c1+gap*dy in [0,3]) or (dy==0 and r1+gap*dx in [0,3]):
                        if visit[r1+gap*dx][c1+gap*dy]==False:
                            next_bfs.append([r1+gap*dx,c1+gap*dy])
                            visit[r1+gap*dx][c1+gap*dy]=True
                    gap+=1
        for x,y in next_bfs:
            if x==r2 and y==c2:
                return cnt+1
            visit[x][y]=True
        cnt+=1
        bfs=next_bfs
    return 999999999999
def dfs(board,r,c,cnt):
    global answer
    cards=card_list(board)
    if not cards:
        answer=min(answer,cnt)
    for fr,fc in cards:
        b=deepcopy(board)
        pic=b[fr][fc]
        b[fr][fc]=0
        pr,pc=[[x,y] for x in range(4) for y in range(4) if b[x][y]==pic][0]
        b[pr][pc]=0
        dfs(b,pr,pc,cnt+move_target(board,r,c,fr,fc)+move_target(board,fr,fc,pr,pc)+2)
def solution(board, r, c):
    global answer
    dfs(board,r,c,0)
    return answer