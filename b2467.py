input()
N = list(map(int,input().split()))
A = [N[0],N[1]]
def bisect_left(idx):
    left = idx+1
    right = len(N) - 1
    while left <= right:
        mid = (right+left)//2
        if N[mid] < -N[idx]:
            left = mid+1
        else:
            right = mid-1
    return left
first = -1
for idx in range(len(N)-1):
    if not first and N[idx]>=0:
        first = idx
        break
    left = bisect_left(idx)
    if idx==left-1:
        break 
    if left == len(N):
        if abs(sum(A)) > abs(N[idx]+N[left-1]):
            A = [N[idx],N[left-1]]
    elif left-1==idx:
        A = sorted([A,[N[idx],N[left]]],key=lambda x:abs(sum(x)))[0]
    else:
        A = sorted([A,[N[idx],N[left]],[N[idx],N[left-1]]],key=lambda x:abs(sum(x)))[0]
print(*A)
