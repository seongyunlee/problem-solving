r=1
for _ in range(3):
    r*=int(input())
cnt={str(i):0 for i in range(10)}
for i in str(r):
    cnt[i]+=1
for v in cnt.values():
    print(v)