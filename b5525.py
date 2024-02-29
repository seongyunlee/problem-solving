N=int(input())
input()
S=input()
now = 0
ans = 0
for i in range(len(S)):
    if now%2==1 and S[i]=="O":
        now+=1
    elif now%2==0 and S[i]=="I":
        now+=1
    elif S[i]=="I":
        now = 1
    else:
        now=0
    if now//2 >= N and now%2==1:
        ans+=1
print(ans)