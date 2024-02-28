N = int(input())
K = list(map(int,input().split()))
if K[0]==0:K=K[1:]
if not K:
    print("NO")
else:
    print("YES")
    print(K[0]*111)