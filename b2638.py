file=open("input.txt")
_,*M=[list(map(int,l.split())) for l in file.readlines()]
drdc=[[0,1],[0,-1],[1,0],[-1,0]]
def two(adj):
    global M
    while adj:
        n_adj=[]
        for r,c in adj:
            if M[r][c]==2:continue
            M[r][c]=2
            for dr,dc in drdc:
                nr=r+dr;nc=c+dc
                if 0<=nr<len(M) and 0<=nc<len(M[0]) and M[nr][nc]==0:
                    n_adj.append([nr,nc])
        adj=n_adj
time=0
two([[0,0]])
while True:
    adj=[]
    cheese=False
    for r in range(len(M)):
        for c in range(len(M[0])):
            if M[r][c]!=1:continue
            cheese=True
            cnt=0
            for dr,dc in drdc:
                nr=r+dr;nc=c+dc
                if 0<=nr<len(M) and 0<=nc<len(M[0]) and M[nr][nc]==2:
                    cnt+=1
            if cnt>1:
                M[r][c]=0
                adj.append([r,c])
    if not cheese:
        print(time)
        break
    two(adj)
    time+=1
                