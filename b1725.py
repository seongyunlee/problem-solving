_,*N=open(0).readlines()
N=list(map(int,N))
S=[[0,0]]
answer=0
for n in N:
    i=0
    while S[-1][0]>n:
        answer=max(answer,S[-1][0]*(i+S[-1][1]))
        _,h=S.pop()
        i+=h
    S.append([n,i+1])
    prev=n
i=0
while S:
    answer=max(answer,S[-1][0]*(i+S[-1][1]))
    n,h=S.pop()
    i+=h
print(answer)
