file=open('input.txt')
from sys import setrecursionlimit
setrecursionlimit(10**6)
n,*lines=open(0).readlines()
n=int(n)
E={i:[] for i in range(1,n+1)}
for l in lines:
    k,*v=map(int,l.split())
    for i in range(0,len(v)-1,2):
        E[k].append([v[i],v[i+1]])
dia=1
def dfs(N,prev):
    global dia
    if len(E[N])==1 and E[N][0][0]==prev:
        return 0
    Ncost=[dfs(a[0],N)+a[1] for a in E[N] if a[0]!=prev]
    print(N,Ncost)
    Ncost.sort(reverse=True)
    if len(Ncost)>1:dia=max(dia,sum(Ncost[:2]))
    return(Ncost[0])
Ncost=[dfs(a[0],1)+a[1] for a in E[1]]
print(Ncost)
Ncost.sort(reverse=True)
if len(Ncost)>1: dia=max(dia,sum(Ncost[:2]))
dia=max(dia,Ncost[0])
print(dia)

