import sys
input = sys.stdin.readline
N,M = map(int,input().split())
L = list(map(int,input().split()))
L.sort()
from itertools import permutations
A= []
for p in permutations(list(range(N)),M):
    A.append([L[i] for i in p])
SA = sorted(A)
LtS = lambda x : " ".join([str(i) for i in x])
A = set()
K=[]
for l in SA:
    s = LtS(l)
    if s in A: continue
    A.add(s)
    K.append(s)
print(*K,sep="\n")
