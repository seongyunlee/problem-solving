primes=[True]*1001
primes[1]=False
input()
for i in range(2,1001):
    if primes[i]:
        for j in range(i+i,1001,i):
            primes[j]=False
print(sum(primes[x] for x in list(map(int,input().split()))))