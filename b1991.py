A={}
for _ in range(int(input())):
    p,l,r=input().split()
    A[p]=[None,None]
    if not l==".":A[p][0]=l
    if not r==".":A[p][1]=r
def preorder(n):
    if n==None:return ""
    return n+preorder(A[n][0])+preorder(A[n][1])
def midorder(n):
    if n==None:return ""
    return midorder(A[n][0])+n+midorder(A[n][1])
def lastorder(n):
    if n==None:return ""
    return lastorder(A[n][0])+lastorder(A[n][1])+n
print(preorder("A"))
print(midorder("A"))
print(lastorder("A"))