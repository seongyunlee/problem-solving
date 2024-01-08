M=[list(input()) for _ in range(int(input()))]
def C(sr,sc,er,ec):
    I=M[sr][sc]
    for r in range(sr,er):
        for c in range(sc,ec):
            if not M[r][c]==I:return False
    return True
def S(sr,sc,er,ec):
    if C(sr,sc,er,ec):
        return M[sr][sc]
    r=[sr,sr+(er-sr)//2,er]
    c=[sc,sc+(ec-sc)//2,ec]
    p=[]
    for i in range(2):
        for j in range(2):
            p.append([r[i]]+[c[j]]+[r[i+1]]+[c[j+1]])
    a=""
    for i in p:
        a+=S(*i)
    return "("+a+")"
print(S(0,0,len(M),len(M)))