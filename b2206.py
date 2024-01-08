S,*M=open('input.txt').readlines()
n,m=map(int,S.split())
M=[list(map(int,list(l.strip()))) for l in M]
V=[[0,0,0]]
drdc=[[-1,0],[1,0],[0,1],[0,-1]]
visit=[[[False,False] for _ in range(m)] for _ in range(n)]
answer=0
while V:
    nV=[]
    for r,c,b in V:
        if visit[r][c][0] or (b==1 and visit[r][c][1]):continue
        visit[r][c][b]=True
        if [r,c]==[n-1,m-1]:
            nV=[]
            break
        for dr,dc in drdc:
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<m:
                if b==0 and M[nr][nc]==1 and not True in visit[nr][nc]:
                    nV.append([nr,nc,1])
                if M[nr][nc]==0 and not visit[nr][nc][b]:
                    nV.append([nr,nc,b])
    V=nV
    answer+=1
print(answer if True in visit[-1][-1] else -1)
