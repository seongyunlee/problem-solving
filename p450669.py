E,N,T,V,R,dp=[None]*6
def getDp(frm,to):
    global dp
    if dp[frm][to]!=-1:return dp[frm][to]
    dp[frm][to]=max([getDp(to,x) for x in E[to] if x!=frm]+[0])+1
    return dp[frm][to]
def solution(t):
    global E,N,T,V,R,dp
    E={i:[] for i in range(len(t)+1)}
    dp=[[-1]*(len(t)+1) for _ in range(len(t)+1)]
    for frm,to in t:
        E[frm].append(to)
        E[to].append(frm)
    answer=0
    for n in range(len(t)+1):
        answer=max(answer,1+sum(sorted([getDp(n,x) for x in E[n]]+[0,0],reverse=True)[:3]))
        print(n,answer,sum([getDp(n,x) for x in E[n]]+[0,0]))
    return answer
print(solution([[5,1],[2,5],[3,5],[3,6],[2,4],[4,0]]))