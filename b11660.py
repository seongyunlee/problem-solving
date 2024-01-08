import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
S=[]
for i in range(N):
    S.append([])
    acc=0
    for j in range(N):
        acc+=A[i][j]
        S[-1].append(acc+(S[i-1][j] if i>0 else 0))
for _ in range(M):
    a,b,c,d=map(int,input().split())
    print(S[c-1][d-1]-(S[a-2][d-1] if a>1 else 0)-(S[c-1][b-2] if b>1 else 0)+(S[a-2][b-2] if a>1 and b>1 else 0))