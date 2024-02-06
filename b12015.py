N = int(input())
A = list(map(int, input().split()))
def find(D, target):
    # find the minimum index i such that D[i] > target
    left = 0
    right = len(D) - 1
    while left < right:
        mid = (left + right) // 2
        if D[mid] > target:
            right = mid
        else:
            left = mid + 1
    if D[left] > target:
        return left
    else:
        return right
D = [A[0]]
M = 1
for a in A[1:]:
    if a > D[-1]:
        D.append(a)
    elif a <= D[0]:
        continue
    else:
        M = max(M, len(D))
        idx = find(D, a)
        if idx==-1:
            D[0] = a
        else:
            D[idx] = a
print(len(D))