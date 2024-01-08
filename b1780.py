N=int(input())
M=[list(map(int,input().split())) for _ in range(N)]
def C(sr,sc,er,ec):
    I=M[sr][sc]
    for r in range(sr,er):
        for c in range(sc,ec):
            if not M[r][c]==I:return False
    return True
def S(sr,sc,er,ec):
    a=[0,0,0]
    if C(sr,sc,er,ec):
        a[M[sr][sc]+1]=1
        return a
    r=[sr,sr+(er-sr)//3,sr+((er-sr)//3)*2,er]
    c=[sc,sc+(ec-sc)//3,sc+((ec-sc)//3)*2,ec]
    p=[]
    for i in range(3):
        for j in range(3):
            p.append([r[i]]+[c[j]]+[r[i+1]]+[c[j+1]])
    for i in p:
        if not C(*i):
            k=S(*i)
            a=[a[i]+k[i] for i in range(3)]
        else:
            a[M[i[0]][i[1]]+1]+=1
    return a
print(*S(0,0,len(M),len(M)),sep="\n")