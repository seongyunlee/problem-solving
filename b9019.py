import sys
input = sys.stdin.readline
def D(x):
    return x*2%10000
def S(x):
    return x-1 if x>0 else 9999
def L(x):
    return x*10%10000+x//1000
def R(x):
    return x//10+x%10*1000
def solve(a,b):
    visit = [False]*10001
    P = [[a,""]]
    while P:
        nP = []
        for p,a in P:
            if p==b:
                return a
            n = [[D(p),a+"D"],[S(p),a+"S"],[L(p),a+"L"],[R(p),a+"R"]]
            for s in n:
                if not visit[s[0]]:
                    nP.append(s)
                    visit[s[0]] = True
        P = nP
ans = []
for _ in range(int(input())):
    ans.append(solve(*map(int,input().split())))
print("\n".join(ans))