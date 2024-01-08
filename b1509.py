from sys import setrecursionlimit
setrecursionlimit(10**7)
w=input()
dp=[None]*len(w)
palin_to=[[i] for i in range(len(w))]
def palin(idx,acc):
    if idx==len(w):return
    for i in range(len(acc)):
        if idx+i>len(w)-1:break
        if acc[-(i+1)]!=w[idx+i]:
            break
        palin_to[idx-i-1].append(idx+i)
    for i in range(len(acc)):
        if idx+i+1>len(w)-1:break
        if acc[-(i+1)]!=w[idx+i+1]:
            break
        palin_to[idx-i-1].append(idx+i+1)
    palin(idx+1,acc+w[idx])
palin(0,'')
def minS(idx):
    if idx==len(w):
        return 0
    if dp[idx]==None:
        dp[idx]=min([1+minS(i+1) for i in palin_to[idx]])
    return dp[idx]
minS(0)
print(dp[0])