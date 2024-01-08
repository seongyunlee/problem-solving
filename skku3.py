N=int(input())
def primes():
    K=[True]*(N+1)
    K[0]=K[1]=False
    for i in range(2,len(K)):
        if K[i]:
            for j in range(i*2,len(K),i):
                K[j]=False
    return [i for i in range(2,len(K)) if K[i]]
P=primes()
left=0
right=len(P)
while left<right:
    mid=(left+right)//2
    print("?",P[mid])
    I=int(input())
    if I==0:
        right=mid
    else:
        left=mid+1
print("!",P[right])