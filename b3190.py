import sys
from queue import deque
input = sys.stdin.readline
N=int(input())
A=[list(map(int,input().split())) for _ in range(int(input()))]
I=[input().split() for _ in range(int(input()))][::-1]
M=[[0]*N for _  in range(N)]
M[0][0]=1
for r,c in A:
    M[r-1][c-1]=3
B=deque([[0,0]])
dir=[1,1]
time=0
def move():
    r,c=B[-1]
    nr= r + (dir[1] if dir[0]==0 else 0)
    nc= c + (dir[1] if dir[0]==1 else 0)
    if not (0<=nr<N and 0<=nc<N):return False
    if M[nr][nc]==1:return False
    B.append([nr,nc])
    if M[nr][nc]!=3:
        r,c=B.popleft()
        M[r][c]=0
    M[nr][nc]=1
    return True

while True:
    if not move():
        print(time+1)
        break
    time+=1
    if I and int(I[-1][0])==time:
        _,D=I.pop()
        dir=[int(not dir[0]),dir[1]*(1 if D=="D" else -1)*(-1 if dir[0]==0 else 1)]



