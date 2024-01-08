input()
N=list(map(int,input().split()))
A=[-1]*len(N)
prev=0
for i in range(len(N)):
    if N[i]!=N[prev]:
        for j in range(prev,i,1):
            A[j]=i+1
        prev=i
print(*A,sep=" ")
