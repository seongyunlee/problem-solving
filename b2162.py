import sys
input = sys.stdin.readline
P = [list(map(int, input().split())) for _ in range(int(input()))]
M = [[i] for i in range(len(P))]
G = list(range(len(P)))
def ccw(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
def intersect(A,B,C,D):
    X = ccw(A,B,C)*ccw(A,B,D)
    Y = ccw(C,D,A)*ccw(C,D,B)
    if X == 0 and Y == 0:
        if A > B:
            A,B = B,A
        if C > D:
            C,D = D,C
        return C <= B and A <= D
    return X <= 0 and Y <= 0
for i in range(len(P)):
    A = P[i][:2]
    B = P[i][2:]
    for j in range(i+1, len(P)):
        if G[i] == G[j]:
            continue
        C = P[j][:2]
        D = P[j][2:]
        if intersect(A,B,C,D):
            smallG = G[i]
            bigG = G[j]
            if len(M[smallG]) > len(M[bigG]):
                smallG, bigG = bigG, smallG
            for k in M[smallG]:
                M[bigG].append(k)
                G[k] = bigG
            M[smallG] = []
A = [i for i in M if i]
print(len(A))
print(max(len(i) for i in A))