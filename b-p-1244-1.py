import sys
input = sys.stdin.readline
for _ in range(int(input())):
    S = input().strip()
    digit = [k for k in S if k in ["0","1"]][0]
    N = 0
    if S[0]=="!" and S[-1]=="!":
        L,R = S.split(digit)
        N = len(L)
    elif S[0]=="!":
        N = len(S)-1
    if S[-1]=="!":
        digit = "1"
    if N%2 == 0: print(digit)
    else: print(1 if digit=="0" else 0)
    