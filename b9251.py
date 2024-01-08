a=input()
b=input()
dp=[[-1]*len(b) for _ in range(len(a))]
def getDp(x,y):
    if dp[x][y]!=-1:return dp[x][y]
    maxB=len(b)
    sol=-1
    for i in range(x+1,len(a)):
        for j in range(y+1,maxB):
            if a[i]==b[j]:
                maxB=j
                sol=max(sol,getDp(i,j)+1)
                break
    if sol==-1:dp[x][y]=1
    else:dp[x][y]=sol
    return dp[x][y]
maxB=len(b)
answer=0
for i in range(len(a)):
    for j in range(maxB):
        if a[i]==b[j] and maxB>j:
            maxB=j
            answer=max(answer,getDp(i,j))
            break
print(answer)