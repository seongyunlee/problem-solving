import sys
sys.setrecursionlimit(1000000)
dp=None
N=None
P={i+j*3+1:[i,j] for j in range(3) for i in range(3)}
P[0]=[1,3]
print(P)
def cost(frm,to):
    if frm==to:return 1
    x1,y1=P[frm]
    x2,y2=P[to]
    if abs(x1-x2)+abs(y1-y2)==1:return 2
    if abs(x1-x2)==1 and abs(y1-y2)==1:return 3
    answer=0
    while x1!=x2 and y1!=y2:
        answer+=3
        x1+=1 if (x1<x2) else -1
        y1+=1 if (y1<y2) else -1
    return answer+2*(abs(x1-x2)+abs(y1-y2))
def getDp(idx,minP,maxP):
    if idx==len(N):return 0
    if dp[idx][minP][maxP]!=-1:return dp[idx][minP][maxP]
    if N[idx] in [minP,maxP]:
        dp[idx][minP][maxP] = 1+getDp(idx+1,minP,maxP)
        return dp[idx][minP][maxP]
    else:
        dp[idx][minP][maxP]= min([cost(minP,N[idx])+getDp(idx+1,min(N[idx],maxP),max(N[idx],maxP)),cost(maxP,N[idx])+getDp(idx+1,min(N[idx],minP),max(N[idx],minP))])
        return dp[idx][minP][maxP]
def solution(numbers):
    global N,dp
    N=list(map(int,list(numbers)))
    dp=[[[-1]*10 for _ in range(10)] for _ in range(len(numbers))]
    return getDp(0,4,6)ß