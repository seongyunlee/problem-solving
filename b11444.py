import sys 
d={1:1,0:0}
sys.setrecursionlimit(1000000)
N=int(input())
def dgn(n):
    if d.get(n)!=None:return d[n]
    if n%2==0:
        K=dgn(n//2)
        d[n]= (K*(K+2*dgn(n//2-1)))%1000000007
    else:
        d[n]=(dgn(n//2+1)**2+dgn(n//2)**2)%1000000007
    return d[n]
print(dgn(N)%1000000007)
