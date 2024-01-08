p=[float(input()) for _ in range(10)]
p.sort(reverse=True)
a=1
for k in p[:9]:
    a*=k
for k in [i for i in range(1,10)]:
    a/=k
print(a*10**9)