N=int(input())
dp=[[[0]*1024 for _ in range(10)] for _ in range(N)]
for i in range(0,N):
    for j in range(10):
        if i==0:
            dp[i][j][2**j]=1
            continue
        for t in [-1,1]:
            if 9>=j+t>=0:
                for k in range(1024):
                    mask=k|(2**j)
                    dp[i][j][mask]+=dp[i-1][j+t][k]
print(sum([dp[N-1][k][1023] for k in range(1,10)])%1000000000)
                    