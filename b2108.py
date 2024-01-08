K,*N=open(0)
N=list(map(int,N))
N.sort()
counter={x:0 for x in N}
for n in N:
    counter[n]+=1
count=[[v,-k] for k,v in counter.items()]
count.sort(reverse=True)
if len(count)>1 and count[1][0]==count[0][0]:
    many=-1*count[1][1]
else:
    many=-1*count[0][1]
print(round(sum(N)/len(N)),N[len(N)//2],many,N[-1]-N[0])