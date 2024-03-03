import sys
input = sys.stdin.readline
N,M = map(int,input().split())
R = {}
for i in range(N+M):
    a,b = map(int,input().split())
    R[a-1] = b-1
visit = [False]*100
P = [0]
cnt = 0
def move(s):
    while True:
        if R.get(s)!=None:
            s = R[s]
            continue
        return s
while P:
    nP = []
    for s in P:
        if s == 99:
            print(cnt)
            exit()
        for i in range(1,7):
            if s+i>99: break
            des = move(s+i)
            if visit[des]: continue
            visit[des] = True
            nP.append(des)
    P = nP
    cnt+=1