N=int(input())
P=[]
def chk(r,c,size):
    for i in range(size):
        for j in range(size):
            if not P[r+i][c+j]==P[r][c]:
                size=size//2
                ta,tb=0,0
                for x in range(2):
                    for y in range(2):
                        a,b=chk(r+x*size,c+y*size,size)
                        ta+=a
                        tb+=b
                return (ta,tb)
    return (1,0) if P[r][c]=='0' else (0,1)
for _ in range(N):
    P.append(input().split())
print(*chk(0,0,N))
