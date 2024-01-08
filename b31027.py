N = int(input())
F = [list(map(int,input().split())) for _ in range(2)]
S = []
for f in F:
    s=[0]
    for ff in f:
        s.append(s[-1]+ff)
    S.append(s)
A = [0,0]
B = [1,N-1]
total = S[0][-1]+S[1][-1]
def calc(isA,A,B):
    x,y = A
    i,j = B
    if x==i:
        center = (y+j-1)//2+1
        T = S[0][center+1] + S[1][center+1]
    else:
        center = (y+j)//2
        T = S[x][center+1] + S[x][center]
    if isA: return T
    else: return total - T
TA = 0
TB = 0
def move(org):
    x,y = org
    return [[x+dx,y+dy] for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]] if 0<=dx+x<2 and 0<=dy+y<N]
for i in range(N):
    A = max(move(A),key = lambda x:calc(True,x,B))
    TA += F[A[0]][A[1]]
    B = max(move(B),key = lambda x:calc(True,A,x))
    TB += F[B[0]][B[1]]
print(TA,TB)