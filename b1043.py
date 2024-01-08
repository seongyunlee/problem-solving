N,M=map(int,input().split())
K=list(map(int,input().split()))[1:]
T=[k in K for k in range(1,N+1)]
P=[list(map(int,input().split()))[1:] for _ in range(M)]
TT=[False]*len(P)
NTT=K
while NTT:
    NNTT=[]
    for n in NTT:
        for i,p in enumerate(P):
            if n in p and not TT[i]:
                TT[i]=True
                NNTT+=p
    NTT=NNTT
print(TT.count(False))       