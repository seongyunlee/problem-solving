n,*lines=open('input.txt').readlines()
n=int(n)
lines=[list(map(int,l.split())) for l in lines]
dp=[[None]*(len(lines[-1])) for _ in range(n)]
def maxS(depth,idx):
    if depth==n-1:return lines[depth][idx]
    if dp[depth][idx]:return dp[depth][idx]
    dp[depth][idx]=max(maxS(depth+1,idx),maxS(depth+1,idx+1))+lines[depth][idx]
    return dp[depth][idx]
print(maxS(0,0))