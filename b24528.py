import sys
from random import randint
sys.setrecursionlimit(2000000)
S=[]
for _ in range(10):
    while True:
        c=chr(randint(97,122))
        if not S or S[-1][0]!=c:break
    S.append([c,randint(1,1000000000)])
S=[['z', 760140385], ['e', 560155727], ['m', 598329902], ['e', 560155727], ['k', 739013909],  ['e', 560155727],['u', 158371459], ['p', 156896452], ['g', 675073331], ['k', 980550489], ['h', 5392182], ['y', 406729727]]
print(S)
'''
N,*lines=open(0).readlines()
for line in lines:
    a,b=line.split()
    S.append([a,int(b)])
'''
dp=[[None]*27 for _ in range(len(S)-1)]+[[S[-1][1] if chr(i+97)!=S[-1][0] else 0 for i in range(26)]+[S[-1][1]]]
for idx in range(len(S)-2,-1,-1):
    for char in range(27):
        if char==26:
            dp[idx][26]=((dp[idx+1][ord(S[idx][0])-97]+1)*(S[idx][1])+dp[idx+1][26])
        if char==(ord(S[idx][0])-97):
            dp[idx][char]=dp[idx+1][char]
        else:
            dp[idx][char] = (S[idx][1]*(dp[idx+1][26]+1)+dp[idx+1][char])
print(dp[0][26]%998244353)