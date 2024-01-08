import sys
input = sys.stdin.readline
A = [list(input().strip()) for _ in range(int(input().split()[0]))]
B = [list(input().strip()) for _ in range(len(A))]
def fill(r,c,org,to):
    if A[r][c]==to.lower():
        return
    A[r][c]=to
    for dr,dc in [[-1,0],[0,-1],[0,1],[1,0]]:
        nr,nc = r+dr,c+dc
        if 0<=nr<len(A) and 0<=nc<len(A[0]) and A[nr][nc]==org:
            fill(nr,nc,org,to)
for r in range(len(A)):
    for c in range(len(A[0])):
        fill(r,c,A[r][c],B[r][c].lower())
        print(*A,sep="\n",end="\n\n")
        print(*B,sep="\n",end="\n\n")
for r in range(len(A)):
    for c in range(len(A[0])):
        if A[r][c]!=B[r][c].lower():
            print("NO")
            exit()
print("YES")