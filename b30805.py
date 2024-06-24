from collections import defaultdict
input()
N = list(map(int, input().split()))
input()
M = list(map(int, input().split()))
A = []
Ndict = defaultdict(list)
Mdict = defaultdict(list)
for i in range(len(N)):
    Ndict[N[i]].append(i)
for j in range(len(M)):
    Mdict[M[j]].append(j)
ans = []
Nidx, Midx = 0, 0
for i in range(100, -1, -1):
    if Ndict[i] and Mdict[i]:
        x,y = 0,0
        while x < len(Ndict[i]) and Ndict[i][x] < Nidx:
            x += 1
        while y < len(Mdict[i]) and Mdict[i][y] < Midx:
            y += 1
        while x < len(Ndict[i]) and y < len(Mdict[i]):
            ans.append(i)
            Nidx = Ndict[i][x]
            Midx = Mdict[i][y]
            x+=1
            y+=1
print(len(ans))
print(*ans)
        