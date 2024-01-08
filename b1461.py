N,M=map(int,input().split())
book=list(map(int,input().split()))
minus=sorted([x for x in book if x<0])
plus=sorted([x for x in book if x>0],reverse=True)
def left():
    if not minus: return 999999999999999
    mminus=list(minus)
    pplus=list(plus)
    walk=0
    walk+=abs(mminus[0])
    mminus=mminus[M:]
    return work(mminus,pplus,walk)
def right():
    if not plus: return 999999999999999
    mminus=list(minus)
    pplus=list(plus)
    walk=0
    walk+=abs(pplus[0])
    pplus=pplus[M:]
    return work(mminus,pplus,walk)
def work(minus,plus,walk):
    while len(minus)>0:
        walk+=2*abs(minus[0])
        minus=minus[min(len(minus),M):]
    while len(plus)>0:
        walk+=2*abs(plus[0])
        plus=plus[min(len(plus),M):]
    return walk
print(min(left(),right()))