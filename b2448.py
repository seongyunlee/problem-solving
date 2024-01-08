import sys
sys.setrecursionlimit(int(1e8))
n=int(input())
k=len(bin(n//3))-2
unit=["  *  "," * * ","*****"]
def star(size):
    if size==1:
        return unit
    return resize(star(size-1),6*(2**(size-1))-1)+[s+" "+s for s in star(size-1)]
def resize(org,size):
    margin=(size-len(org[0]))//2
    resized=[]
    for i in range(len(org)):
        resized.append(" "*margin+org[i]+" "*margin)
    return resized
print(*star(k),sep="\n")