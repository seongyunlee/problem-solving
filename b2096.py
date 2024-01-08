m=int(input())
a,b,c=0,0,0
d,e,f=0,0,0
for _ in range(m):
    x,y,z = map(int,input().split())
    a,b,c=max(a,b)+x,max([a,b,c])+y,max(b,c)+z
    d,e,f=min(d,e)+x,min([d,e,f])+y,min(e,f)+z
print(max(a,b,c),min(d,e,f))