N = int(input())
A = list(map(int, input().split()))
def find(D, target):
    # find the largest index i such that D[i] < target
    l, r = 0, len(D)-1
    while l<r:
        mid = (l+r)//2
        if D[mid] < target:
            l = mid+1
        else:
            r = mid
    if D[r] < target:
        return r
    else:
        return l
D = [A[0]]
M = [(A[0], 1)]
for a in A[1:]:
    if a > D[-1]:
        D.append(a)
        M.append((a, len(D)))
    elif a in [D[0], D[-1]]:
        continue
    else:
        idx = find(D, a)
        if idx==-1:
            D[0] = a
        else:
            D[idx] = a
        M.append((a, idx+1))
ans = len(D)
P = []
print(ans)
while ans and M:
    num, idx = M.pop()
    if idx == ans:
        P.append(num)
        ans -= 1
print(*P[::-1])