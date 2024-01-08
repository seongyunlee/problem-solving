from random import randint
import bisect

B=[randint(-100,100) for _ in range(5)]*2
B.sort()
print(B)
def bisect_left(t):
    l=0
    r=len(B)
    while r-l>0:
        mid=(l+r)//2
        if B[mid]<t:
            l=mid+1
        else:
            r=mid
    return l
def bisect_right(t):
    l=0
    r=len(B)
    while r-l>1:
        mid=(l+r)//2
        if B[mid]<t:
            l=mid+1
        else:
            r=mid
    return r
def S(t):
    print(bisect_left(t),bisect_right(t))