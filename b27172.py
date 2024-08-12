N = int(input())
A = list(map(int,input().split()))
primes = []
def initPrimes(n):
    A = [True]*(n+1)
    A[0] = A[1] = False
    for i in range(2,n+1):
        if A[i]:
            primes.append(i)
            for j in range(i*i,n+1,i):
                A[j] = False

def factorize(n):
    T = {}
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            if not p in T:
                T[p] = 0
            T[p] += 1
            n //= p
    if n > 1:
        if not n in T:
            T[n] = 0
        T[n] += 1
    keys = []
    values = []
    for k in sorted(T.keys()):
        keys.append(k)
        values.append(T[k])
    return [keys,values]
def plusOne(ref,now):
    for i in range(len(ref)):
        if ref[i] > now[i]:
            now[i] += 1
            return True
        else:
            now[i] = 0
    return False
def mult(factor,pow):
    res = 1
    for i in range(len(factor)):
        res *= factor[i]**pow[i]
    return res
initPrimes(10**6)
ans = [0]*N
orgIdx = {i:idx for idx,i in enumerate(A)}
visited = {}
A.sort()
for idx,a in enumerate(A):
    keys,values = factorize(a)
    now = [0]*len(keys)
    while True:
        factor = mult(keys,now)
        if factor in visited:
            ans[orgIdx[factor]] += 1
            ans[orgIdx[a]] -= 1
        if not plusOne(values,now):
            break
    visited[a] = idx
print(*ans)