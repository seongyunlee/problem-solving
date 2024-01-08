N=int(input())
a=1
d=1
nm=False
nr=0
while N>1:
    if nm==False:
        a=a+d
    NN=N//2+(1 if nm and N%2==1 else 0)
    nm=nm if N%2==0 else not nm
    d=d*2
    N=NN
print(a)
print(int(bin(int(i:=input())*42)[3:],2)or i)