S=input()
T=input()
C=[[] for _ in range(26)]
for i in range(len(S)-1,-1,-1):
    C[ord(S[i])-97].append(i)
A=0
while True:
    prev=-1
    ok=False
    for i in range(len(T)):
        idx=ord(T[i])-97
        nt=False
        while C[idx]:
            pos=C[idx].pop()
            if pos>prev:
                prev=pos
                if i==len(T)-1:
                    A+=1    
                    ok=True 
                nt=True
                break
        if not nt:break
    if not ok:break
print(A)