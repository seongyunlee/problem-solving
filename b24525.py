'''
from random import randint
S="".join([chr(randint(ord('A'),ord('Z'))) for _ in range(10000)])
print(S)
'''
import sys
sys.setrecursionlimit(100001)
S=input()
ans=-1
diff=[0]*len(S)
r={0:-1}
acc=0
for i in range(len(S)):
    if S[i]=="K":acc+=1
    if S[i]=="S":acc-=2
    diff[i]=acc
ok={}
for i in range(len(S)):
    if r.get(diff[i])!=None:
        if (i>0 and diff[i]!=diff[i-1]) or ok.get(diff[i]):
            ans=max(ans,i-r[diff[i]])
            ok[diff[i]]=True
            print(i,ans,diff[i])
    else:
        r[diff[i]]=i
print(ans)