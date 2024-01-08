R,C = map(int,input().split())
B=[list(input()) for _ in range(R)]
M=lambda x,y:2**(ord(B[x][y])-ord('A'))
P={(0,0,M(0,0))}
answer=0
while P:
    answer+=1
    NP=[]
    for r,c,m in P:
        for x,y in [(-1,0),(0,1),(0,-1),(1,0)]:
            if 0<=r+x<R and 0<=c+y<C and m&M(r+x,c+y)==0:
                NP.append((r+x,c+y,m|M(r+x,c+y)))
    P={*NP}
print(answer)