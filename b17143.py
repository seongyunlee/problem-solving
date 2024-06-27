import sys
input = sys.stdin.readline
R,C,M = map(int,input().split())
A = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    A[r-1][c-1].append((s,d,z,-1))

drdc = [(-1,0),(1,0),(0,1),(0,-1)]
reverse = [2,1,4,3]

ans = 0

for t in range(C):
    for r in range(R):
        if A[r][t]:
            s,d,z,_ = A[r][t][0]
            A[r][t] = []
            ans += z
            break
    for r in range(R):
        for c in range(C):
            if A[r][c]:
                orgA = [k for k in A[r][c] if k[-1]!=t]
                A[r][c] = [k for k in A[r][c] if k[-1]==t]
                for s,d,z,p in orgA:
                    dr,dc = drdc[d-1]
                    nr = (R-1)-abs((dr*s+r)%(2*R-2)-R+1)
                    nc = (C-1)-abs((dc*s+c)%(2*C-2)-C+1)
                    if (dr*s+r)%(2*R-2) >= R or (dc*s+c)%(2*C-2) >= C:
                        d = reverse[d-1]
                    A[nr][nc].append((s,d,z,t))
    for r in range(R):
        for c in range(C):
            if len(A[r][c]) > 1:
                A[r][c] = [max(A[r][c],key=lambda a:a[2])]

print(ans)