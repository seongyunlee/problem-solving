import sys
import math
input = sys.stdin.readline
D = [list(map(int,input().split())) for _ in range(int(input()))]
def pow(x,y):
    if y == 0:
        return 1
    if y%2:
        return (pow(x,y-1)*x)%MOD
    a = pow(x,y//2)
    return (a*a)%MOD
MOD = 1000000007
ans = 0
for x,y in D:
    gcd = math.gcd(x,y)
    x //= gcd
    y //= gcd
    ans += y*pow(x,MOD-2)%MOD
    ans %= MOD
print(ans) 
