from math import comb
A=dp=N=None
def getDp(row,gap):
    print(row,gap)
    if row==len(A):
        if gap==N:return 1
        else: return 0
    if dp[row][gap+N]!=None:
        return dp[row][gap+N]
    print(row,[i for i in range(max(0,A[row]-(N-gap)//2),min(A[row],(N+gap)//2)+1)])
    dp[row][gap+N]=sum([getDp(row+1,gap+2*A[row]-4*i)*comb((N+gap)//2,i)*comb((N-gap)//2,A[row]-i) for i in range(max(0,A[row]-(N-gap)//2),min(A[row],(N+gap)//2)+1)]+[0])
    return dp[row][gap+N]
def solution(a):
    global dp,A,N
    N=len(a)
    A=[[a[i][j] for i in range(len(a))].count(1) for j in range(len(a[0]))]
    dp=[[None]*(N*2+1) for _ in range(len(A))]
    return getDp(0,N)
print(solution(		[[1, 0, 0], [1, 0, 0]]))
print(dp)