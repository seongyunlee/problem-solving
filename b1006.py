import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
memo,P,N,W = [None]*4
def dp(top,bottom,tr,br):
    if top==N-tr and bottom==N-br:
        return 0
    if top==N-tr:
        if br == 0 and bottom == N-2:
            return 1 if P[1][-1]+P[1][-2]<=2 else 2
        return 1
    if memo[top][bottom-top+2][tr*2+br] != None:
        return memo[top][bottom-top+2][tr*2+br]
    if top==0:
        C = [dp(1,0,0,0)]
        if P[0][1]+P[0][0]<=W:
            C.append(dp(2,0,0,0))            
        if P[0][0]+P[0][-1]<=W:
            C.append(dp(1,0,1,0))
        if P[0][0]+P[1][0]<=W:
            C.append(dp(1,1,0,0))
        memo[top][bottom-top+2][tr*2+br] = min(C)+1
        return memo[top][bottom-top+2][tr*2+br]
    if bottom==0:
        C = [dp(top,1,tr,0)]
        if P[1][0]+P[1][-1]<=W:
            C.append(dp(top,1,tr,1))
        if P[1][0]+P[1][1]<=W:
            C.append(dp(top,2,tr,0))
        memo[top][bottom-top+2][tr*2+br] =  min(C)+1
        return memo[top][bottom-top+2][tr*2+br]
    if top<=bottom:
        C = []
        if top+1<=N-tr:
            C.append(dp(top+1,bottom,tr,br))
        if top+2<=N-tr and P[0][top]+P[0][top+1]<=W:
            C.append(dp(top+2,bottom,tr,br))
        if top==bottom and top+1<=N-tr and bottom+1<=N-br and P[0][top]+P[1][bottom]<=W:
            C.append(dp(top+1,bottom+1,tr,br))
        memo[top][bottom-top+2][tr*2+br] =  min(C)+1
        return memo[top][bottom-top+2][tr*2+br]
    else:
        C = []
        if bottom+1 <= N-br:
            C.append(dp(top,bottom+1,tr,br))
        if bottom+2 <= N-br and P[1][bottom]+P[1][bottom+1]<=W:
            C.append(dp(top,bottom+2,tr,br))
        memo[top][bottom-top+2][tr*2+br] = min(C)+1
        return memo[top][bottom-top+2][tr*2+br]
    
for i in range(int(input())):
    N,W = map(int,input().split())
    
    P = [list(map(int,input().split())) for _ in range(2)]
    if N==1:
        if P[0][0]+P[1][0]<=W:
            print(1)
        else:
            print(2)
        continue
    memo = [[[None,None,None,None] for _ in range(4)] for _ in range(N)]
    print(dp(0,0,0,0))