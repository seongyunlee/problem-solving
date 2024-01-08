import sys
input=sys.stdin.readline
for _ in range(int(input())):
    dp=[[0]*3 for _ in range(int(input())+1)]
    M=[list(map(int,input().split())) for _ in range(2)]
    for i in range(len(dp)-2,-1,-1):
        dp[i][0]=max([dp[i+1][x] for x in [0,1,2]])
        dp[i][1]=M[0][i]+max([dp[i+1][x] for x in [0,2]])
        dp[i][2]=M[1][i]+max([dp[i+1][x] for x in [0,1]])
    print(max([dp[0][x] for x in range(3)]))