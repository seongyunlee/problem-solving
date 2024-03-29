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
M = 1
for a in A[1:]:
    if a > D[-1]:
        D.append(a)
    elif a in [D[0], D[-1]]:
        continue
    else:
        M = max(M, len(D))
        idx = find(D, a)
        if idx==-1:
            D[0] = a
        else:
            D[idx] = a
print(len(D))