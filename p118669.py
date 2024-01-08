import sys
sys.setrecursionlimit(10000000)
alt,cot,P=[None]*3
dp=[[-1]*151 for _ in range(151)]
def getDp(al,co):
    print(al,co)
    if al>=alt and co>=cot:return 0
    if dp[al][co]!=-1:return dp[al][co]
    C=[]
    for p,q,r,s,t in P:
        if al>=alt and s==0:continue
        if co>=cot and r==0:continue
        if p>al or q>co:continue
        C.append(t+getDp(min(150,al+r),min(150,co+s)))
    dp[al][co]=min(C)
    return dp[al][co]
def solution(alp, cop, problems):
    global alt,cot,P
    P=problems+[[0,0,1,0,1],[0,0,0,1,1]]
    alt=max([x[0] for x in problems])
    cot=max([x[1] for x in problems])
    return getDp(alp,cop)
print(solution(10	,10	,[[10,15,2,1,2],[20,20,3,3,4]]))