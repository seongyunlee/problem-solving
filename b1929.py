primes=[True]*1000000
primes[1]=False
f,t=map(int,input().split())
for i in range(2,t+1):
    if primes[i]:
        for j in range(i+i,t+1,i):
            primes[j]=False
print(*[x for x in range(f,t+1) if primes[x]],sep="\n")