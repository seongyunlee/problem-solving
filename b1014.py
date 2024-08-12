import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
drdc = [(-1,-1),(0,-1),(0,1),(-1,1)]
a, b = 0, 0
dp = None
M = None
ans = 0
possible_bit = None
def getDP(r,bit):
    if dp[r][bit] != -1:
        return dp[r][bit]
    if any(M[r][i] == 'x' and (bit>>i)&1 for i in range(b)):
        dp[r][bit] = 0
        return 0
    if r == 0:
            dp[r][bit] = bin(bit).count('1')
            return dp[r][bit]
    minBit = (bit<<1) | (bit>>1)
    for pb in possible_bit:
        if minBit & pb != 0:
            continue
        dp[r][bit] = max(dp[r][bit],getDP(r-1,pb)+bin(bit).count('1'))
    dp[r][bit] = max(dp[r][bit],0)
    return dp[r][bit]
A = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = 0
    M = [input() for _ in range(a)]
    possible_bit = []
    for i in range(2**b):
        if not bin(i).count('11'):
            possible_bit.append(i)
    dp = [[-1] * (2**b) for _ in range(a)]
    A.append(max(getDP(a-1,bit) for bit in possible_bit))
print('\n'.join(str(a) for a in A))

