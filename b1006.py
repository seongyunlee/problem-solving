import sys
input = sys.stdin.readline
N = int(input())
answers = []
for _ in range(N):
    A, W = map(int,input().split())
    E = [list(map(int,input().split())) for _ in range(2)]
    if A==1:
        answers.append(1 if E[0][0]+E[1][0] <= W else 2)
        continue
    ans = A*2
    for i in range(4):
        # i:0 16,8/ 9,1 사이에 연결 없음
        # i:1 16,8/ 9,1 사이에 바깥쪽 연결
        # i:2 16,8/ 9,1 사이에 안쪽 연결
        # i:3 16,8/ 9,1 사이에 모두 연결
        dp = [[0,0,0] for _ in range(A)]
        if i == 0:
            dp[0][0] = 2 if E[0][0] + E[1][0] > W else 1
            dp[0][1] = dp[0][2] = 1
        if i == 1:
            if E[0][-1] + E[0][0] > W: continue
            dp[0][0] = 2
            dp[0][1] = 1
            dp[0][2] = 2*A
        if i == 2:
            if E[1][-1] + E[1][0] > W: continue
            dp[0][0] = 2
            dp[0][1] = 2*A
            dp[0][2] = 1
        if i == 3:
            if E[0][-1] + E[0][0] > W or E[1][-1] + E[1][0] > W: continue
            dp[0][0] = 2
            dp[0][1] = dp[0][2] = 2*A
        for k in range(1,A - (1 if i != 0 else 2 if i == 3 else 0)):
            dp_k0 = []
            # 전 단계에서 꽉 찼을 때
            dp_k0.append(dp[k-1][0]+(1 if E[0][k] + E[1][k] <= W else 2))
            # 전 단계에서 바깥쪽만 찼고, 이번에 안쪽 연결
            if E[1][k-1] + E[1][k] <= W:
                dp_k0.append(dp[k-1][1]+2)
            # 전 단계에서 안쪽만 찼고, 이번에 바깥쪽 연결
            if E[0][k-1] + E[0][k] <= W:
                dp_k0.append(dp[k-1][2]+2)
            # 둘다 연결 가능할 때
            if E[0][k-1] + E[0][k] <= W and E[1][k-1] + E[1][k] <= W and (k>1 or i==0):
                dp_k0.append((dp[k-2][0] if k>1 else 0)+2)
            dp_k1 = []
            # 전 단계에서 꽉 찼을 때
            dp_k1.append(dp[k-1][0]+1)
            # 전 단계에서 안쪽만 찼고, 이번에 바깥쪽 연결
            if E[0][k-1] + E[0][k] <= W:
                dp_k1.append(dp[k-1][2]+1)
            dp_k2 = []
            # 전 단계에서 꽉 찼을 때
            dp_k2.append(dp[k-1][0]+1)
            # 전 단계에서 바깥쪽만 찼고, 이번에 안쪽 연결
            if E[1][k-1] + E[1][k] <= W:
                dp_k2.append(dp[k-1][1]+1)
            dp[k][0] = min(dp_k0)
            dp[k][1] = min(dp_k1)
            dp[k][2] = min(dp_k2)
        if i==1:
            dp_last_0 = []
            dp_last_0.append(dp[-2][0]+1)
            if E[1][-1]+E[1][-2] <= W:
                dp_last_0.append(dp[-2][1]+1)
            ans = min(ans,min(dp_last_0))
        elif i==2:
            dp_last_0 = []
            dp_last_0.append(dp[-2][0]+1)
            if E[0][-1]+E[0][-2] <= W:
                dp_last_0.append(dp[-2][2]+1)
            ans = min(ans,min(dp_last_0))
        elif i==3:
            ans = min(ans,dp[-2][0])
        else:
            ans = min(ans,dp[-1][0])
    answers.append(ans)
print(*answers,sep='\n')

            
            


            
