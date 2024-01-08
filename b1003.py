dp=[None]*41
dp[0]=[1,0]
dp[1]=[0,1]
def solution(N):
    if dp[N]==None:
        dp[N]=[x+y for x,y in zip(solution(N-1),solution(N-2))]
    return dp[N]
for _ in range(0,int(input())):
    A=solution(int(input()))
    print(A[0],A[1])
