N=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())
ceil = lambda x : int(x//1 if x%1==0 else x//1+1)
print(sum([1+ceil(max(0,x-B)/C) for x in A]))