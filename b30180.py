import sys
from queue import heappop,heappush
input = iter(open(0).read().split("\n")).__next__
H,W,N = map(int,input().split())
S = [list(map(int,input().split())) for _ in range(H)]
answer = -1
for w in range(1,min(N,W+1)):
    if N%w!=0 or N//w>H:continue
    cnt = {}
    high = []
    low = []
    for i in range(N//w):
        for j in range(w):
            if cnt.get(S[i][j])==None:
                cnt[S[i][j]] = 1
            else: 
                cnt[S[i][j]] += 1
            heappush(high,-S[i][j])
            heappush(low,S[i][j])
    answer = max(-high[0]-low[0],answer)
    for r in range(N//w,H+1):
        Range = range(w,W) if (r-N//w)%2==0 else range(W-w,-1,-1)
        for c in Range:
            appendCol = c
            removeCol = c-w if (r-N//w)%2==0 else c+w-1
            for rr in range(r-N//w,r):
                heappush(high,-S[rr][appendCol])
                heappush(low,S[rr][appendCol])
                cnt[S[rr][removeCol]] -= 1
                if cnt.get(S[rr][appendCol])==None:
                    cnt[S[rr][appendCol]] = 1
                else: 
                    cnt[S[rr][appendCol]] += 1
            while cnt[-high[0]]==0:
                heappop(high)
            while cnt[low[0]]==0:
                heappop(low)            
            answer = max(-high[0]-low[0],answer)
        if r == H:break
        Range = range(W-w,W) if (r-N//w)%2==0 else range(w)
        for c in Range:
            cnt[S[r-N//w][c]] -= 1
            heappush(high,-S[r][c])
            heappush(low,S[r][c])
            if cnt.get(S[r][c])==None:
                cnt[S[r][c]] = 1
            else: 
                cnt[S[r][c]] += 1
            while cnt[-high[0]]==0:
                heappop(high)
            while cnt[low[0]]==0:
                heappop(low)
        answer = max(-high[0]-low[0],answer)
print(answer if N!=1 else 0)