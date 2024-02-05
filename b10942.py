import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
T = int(input())
N = list(map(int, input().split()))
M = [[None]*T for _ in range(T)]
def solve(f,t):
    if M[f][t] is not None:
        return M[f][t]
    if f==t:
        M[f][t] = True
    elif t-f==1:
        M[f][t] = N[f]==N[t]
    elif N[f]==N[t]:
        M[f][t] = solve(f+1,t-1)
    return M[f][t]
A = []
for _ in range(int(input())):
    a,b = map(int, input().split())
    A.append(solve(a-1,b-1))
print('\n'.join(['1' if x else '0' for x in A]))