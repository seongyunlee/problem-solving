import sys
input = sys.stdin.readline
T = [input().strip() for _ in range(int(input()))]
chk = [[False]*len(L) for L in T]
for r in range(len(T)-1):
    for c in range(len(T[r])):
        if chk[r][c]: continue
        if T[r][c] == "R":
            if "B" in [T[r+1][c],T[r+1][c+1]] or True in [chk[r+1][c],chk[r+1][c+1]]:
                print(0)
                exit()
            chk[r+1][c] = True
            chk[r+1][c+1] = True
        else:
            if c==len(T[r])-1 or "R" in [T[r+1][c+1],T[r][c+1]] or True in [chk[r+1][c+1],chk[r][c+1]]:
                print(0)
                exit()
            chk[r+1][c+1] = True
            chk[r][c+1] = True
print(1 if all(chk[-1]) else 0)