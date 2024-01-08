import sys
input=sys.stdin.readline
sys.setrecursionlimit(300000)
o=sorted([list(map(int,input().split())) for _ in range(int(input()))])
k=[]
left=right=0
for l,r in o:
    if l<=right:
        right=max(r,right)
    else:
        k.append([left,right])
        left=l
        right=r
k.append([left,right])
dp=[-1]*len(k)

def dfs(i):
    if dp[i]!=-1:return dp[i]
    a=[k[i][1]]
    for nxt in range(i+1,len(k)):
        if k[i][1]-k[i][0]>=k[nxt][0]-k[i][1]:
            a.append(dfs(nxt))
        else:break
    dp[i]=max(a)
    return dp[i]
print(dfs(0)) 