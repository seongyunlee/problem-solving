R,C=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(R)]
def getMask(r,c):
    M=[]
    M.append([(x,c) for x in range(r,r+4)])
    M.append([(r,x) for x in range(c,c+4)])
    M.append([(x,y) for x in range(r,r+2) for y in range(c,c+2)])
    M.append([(x,c) for x in range(r,r+3)]+[(r,c-1)])
    M.append([(x,c) for x in range(r,r+3)]+[(r,c+1)])
    M.append([(x,c) for x in range(r-2,r+1)]+[(r,c-1)])
    M.append([(x,c) for x in range(r-2,r+1)]+[(r,c+1)])
    M.append([(r,x) for x in range(c,c+3)]+[(r+1,c)])
    M.append([(r,x) for x in range(c,c+3)]+[(r-1,c)])
    M.append([(r,x) for x in range(c-2,c+1)]+[(r+1,c)])
    M.append([(r,x) for x in range(c-2,c+1)]+[(r-1,c)])
    M.append([(r,c),(r+1,c),(r+1,c+1),(r+2,c+1)])
    M.append([(r,c),(r+1,c),(r+1,c-1),(r+2,c-1)])
    M.append([(r,c),(r,c+1),(r+1,c+1),(r+1,c+2)])
    M.append([(r,c),(r,c+1),(r-1,c+1),(r-1,c+2)])
    M.append([(r,x) for x in range(c-1,c+2)]+[(r+1,c)])
    M.append([(r,x) for x in range(c-1,c+2)]+[(r-1,c)])
    M.append([(x,c) for x in range(r-1,r+2)]+[(r,c+1)])
    M.append([(x,c) for x in range(r-1,r+2)]+[(r,c-1)])
    return M
def rotate():
    global B
    B=[[B[len(B)-c+-1][r] for c in range(len(B))] for r in range(len(B[0]))]
def mirrorH():
    global B
    B=[[B[len(B)-r-1][c] for c in range(len(B[0]))] for r in range(len(B))]
def mirrorV():
    global B
    B=[[B[r][len(B[0])-c-1] for c in range(len(B[0]))] for r in range(len(B))]
def match(mask):
    return sum([B[x][y] for x,y in mask])
ans=0
for r in range(len(B)):
    for c in range(len(B[0])):
        for i,mask in enumerate(getMask(r,c)):
            if all([0<=x<len(B) and 0<=y<len(B[0]) for x,y in mask]):
                if ans<(K:=match(mask)):
                    ans=K
print(ans)
