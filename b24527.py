import sys
from bisect import bisect_right
input=sys.stdin.readline
H=int(input())+1
Q,R=map(int,input().split())
F=[i*(i-1)//2+1 for i in range(1,H+1)]
sumE=[]
answer=[]
E=[0]*(H+2)
def getRC(idx):
    return bisect_right(F,idx)
def getLR(idx):
    global H
    r=getRC(idx)
    ld=(r+H-1)*(H-r)//2
    rd=(r+H+1)*(H-r)//2
    return [idx+ld-H*(H-1)//2-1,idx+rd-H*(H-1)//2-1]
def drop(a,b):
    left,right=getLR(a)
    E[left]+=b/(right-left+1)
    if right<len(E):E[right+1]-=b/(right-left+1)
def getE(a,b):
    S=sumE[b-1]-(sumE[a-2] if a-2>=0 else 0)
    return S
for _ in range(Q):
    a,b=map(int,input().split())
    drop(a,b)
for e in E:
    sumE.append(e+(sumE[-1] if sumE else 0))
for i in range(len(sumE)):
    sumE[i]=sumE[i]+(sumE[i-1] if i>0 else 0)
answer=[]
for _ in range(R):
    a,b=map(int,input().split())
    answer.append(getE(a,b))
print(*answer,sep="\n")