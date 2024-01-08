org=[list(map(int,list(input()))) for _ in range(9)]
NN=[[r,c] for r in range(9) for c in range(9)]
boxPos=[[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]], [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]], [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]], [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]], [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]], [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]], [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]], [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]], [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]]
def possible(MM,r,c,n):
    for i in range(9):
        if MM[r][i]==n:return False
        if MM[i][c]==n:return False
    for r,c in boxPos[r//3*3+c//3]:
        if MM[r][c]==n: return False
    return True
def solve(M):
    global org
    for r,c in NN:
        if M[r][c]!=0:continue
        for i in range(1,10):
            if possible(M,r,c,i):
                MM=[line[:] for line in M]
                MM[r][c]=i
                if solve(MM):
                    org[r][c]=i
                    return True
        return False
    return True
solve(org)
print(*map("".join,[[str(k) for k in l] for l in org]),sep="\n")