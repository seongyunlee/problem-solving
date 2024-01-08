from sys import stdin
N,M=map(int,input().split())
name={}
idx=[]
for i in range(N):
    idx.append(A:=stdin.readline().strip())
    name[A]=i
for k in range(M):
    if (A:=stdin.readline().strip()).isdigit():
        print(idx[int(A)-1])
    else:
        print(name[A]+1)