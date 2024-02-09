import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    T  = {}
    for _ in range(int(input())):
        a,b = input().split()
        if b in T:
            T[b].append(a)
        else:
            T[b] = [a]
    A = 1
    for k,v in T.items():
        A *= len(v)+1
    print(A-1)
