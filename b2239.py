from copy import deepcopy
M=[list(map(int,list(input()))) for _ in range(9)]
NN=[[r,c] for r in range(9) for c in range(9)]
def boxPos(r,c):
    pos=[]
    for i in range(3):
        for j in range(3):
            pos.append([r//3*3+i,c//3*3+j])
    return pos
def print_candi(cd):
    buffer=[""]*3
    for r in range(9):
        for c in range(9):
            for i in range(1,10):
                buffer[(i-1)//3]+=str(i) if cd[r][c] and i in cd[r][c] else " "
            for i in range(0,3):
                buffer[i]+="|"
        print(*buffer,sep="\n",end="\n------------------------------------\n")
        buffer=[""]*3
    print("\n\n\n")
def find_candi(r,c):
    C=[False]*9
    for i in range(9):
        if M[r][i]!=0:C[M[r][i]-1]=True
        if M[i][c]!=0:C[M[i][c]-1]=True
    for r,c in boxPos(r,c):
        if M[r][c]!=0:
            C[M[r][c]-1]=True
    return [i+1 for i,c in enumerate(C) if c==False]
def set_candi():
    candies=[[None]*9 for _ in range(9)]
    for r in range(9):
        for c in range(9):
            if M[r][c]==0:candies[r][c]=find_candi(r,c)
    return candies
def deter(candi,r,c,d):
    global M
    for i in range(9):
        if i==c:continue
        if candi[r][i] and d in candi[r][i]:
            candi[r][i].remove(d)
            if len(candi[r][i])==1:
                if not deter(candi,r,i,cd:=candi[r][i][0]): return False
                else:candi[r][i]=None;M[r][i]=cd
            elif len(candi[r][i])==0:
                return False
    for i in range(9):
        if i==r:continue
        if candi[i][c] and d in candi[i][c]:
            candi[i][c].remove(d)
            if len(candi[i][c])==1:
                if not deter(candi,i,c,cd:=candi[i][c][0]): return False
                else:candi[i][c]=None;M[i][c]=cd  
            elif len(candi[i][c])==0:
                return False
    for i,j in boxPos(r,c):
        if [i,j]==[r,c]:continue
        if candi[i][j] and d in candi[i][j]:
            candi[i][j].remove(d)
            if len(candi[i][j])==1:
                if not deter(candi,i,j,cd:=candi[i][j][0]): return False
                else:candi[i][j]=None;M[i][j]=cd
            elif len(candi[i][j])==0:
                return False
    return True
def choose_candi(candi):
    global M
    for r,c in NN:
        if candi[r][c]:
            for choose in candi[r][c]:
                new_candi=deepcopy(candi)
                if deter(new_candi,r,c,choose):
                    new_candi[r][c]=None
                    if choose_candi(new_candi):
                        M[r][c]=choose
                        return True
            return False
sc=set_candi()
for r,c in NN:
    if sc[r][c] and len(sc[r][c])==1:
        deter(sc,r,c,sc[r][c][0])
        M[r][c]=sc[r][c][0]
        sc[r][c]=None
choose_candi(sc)
print(*map("".join,[[str(k) for k in l] for l in M]),sep="\n",end="\n\n")