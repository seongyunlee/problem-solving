import sys
input = sys.stdin.readline
L = []
for i in range(int(input())):
    L.append(list(map(int,input().split())))
M = [[0,[]]] + [[500001,[]] for _ in range(len(L))]
L.sort()
def find(arr, x):
    l, r = 0, len(arr)
    # find the first element that is smaller than x
    while l<r:
        m = (l+r)//2 + (1 if (l+r)%2==1 else 0)
        if arr[m][0] < x:
            l = m
        else:
            r = m - 1
    return l
for idx,v in L:
    i = find(M,v)
    if M[i][0] < v < M[i+1][0]:
        M[i+1][0] = v
        M[i+1][1] = M[i][1] + [idx]
for i in range(len(M)-1,0,-1):
    if M[i][1] != []:
        S = set(M[i][1])
        print(len(L)-len(S))
        A = []
        for k in sorted([x[0] for x in L]):
            if k not in S:
                A.append(k)
        print('\n'.join(map(str,A)))
        exit()