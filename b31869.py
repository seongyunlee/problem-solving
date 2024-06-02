n = int(input())
by = {}
byl = [input().split() for _ in range(n)]
byl.sort(key=lambda x: (int(x[1])*7 + int(x[2])))
sbn = {}
for _ in range(n):
    a,b = input().split()
    sbn[a] = int(b)
prv = 0
ans = 0
mAns = 0
for name, w, d, c in byl:
    w,d,c = int(w),int(d),int(c)
    if sbn[name] < c:
        continue
    if w*7 + d == prv:
        continue
    if w*7 + d == prv + 1:
        ans += 1
    else:
        mAns = max(mAns, ans)
        ans = 1
    prv = w*7 + d
print(max(mAns, ans))
