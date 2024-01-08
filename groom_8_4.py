import sys
sys.setrecursionlimit(100)
N,K = map(int,input().split())
E={i:[] for i in range(N+1)}
for _ in range(N-1):
	f,t= map(int,input().split())
	E[f].append(t)
	E[t].append(f)
A=list(map(int,input().split()))
answer=0
print(E)
def dfs(idx,k,visit):
	global answer
	answer=max(answer,k)
	print(idx,visit)
	visit[idx]=True
	for i in E[idx]:
		if not visit[i]:
			if k+A[idx-1]<=K:
				dfs(i,k+A[idx-1],list(visit))
			dfs(i,k,list(visit))
dfs(1,0,[False]*(N+1))
print(answer)