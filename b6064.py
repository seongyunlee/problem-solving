import sys
def GCD(x,y):
    while y:
        x,y = y,x%y
    return x
def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result
def calc(M,N,X,Y):
    limit = (LCM(M,N)-Y)//N
    for i in range(limit+1):
        T = N*i + Y - X
        if T<=0: continue
        if T%M==0:
            return N*i+Y
    return -1
for _ in range(int(input())):
    M,N,X,Y = map(int,sys.stdin.readline().strip().split())
    print(calc(M,N,X,Y))
