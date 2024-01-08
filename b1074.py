N,r,c=map(int,input().split())
br=bin(r)[2:].zfill(N)
bc=bin(c)[2:].zfill(N)
print(int(''.join([br[i]+bc[i] for i in range(N)]),2))
