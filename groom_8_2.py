input()
H=list(map(int,input().split()))
sl=[]
def insert(h):
	global sl
	if not sl or sl[-1]==h:
		sl.append(h)
		return len(sl)-1
	s=0
	e=len(sl)-1
	mid= (s+e)//2
	while True:
		if sl[mid]<=h:
			s=mid
		else:
			e=mid
		mid = (s+e)//2
		if mid==s:
			sl=sl[:e]+[h]+sl[e:]
			return e
prev=H[0]
more=0
acc=0
for h in H:
	print(more+acc,end=" ")
	acc+=1
	if prev<h:
		idx=insert(h)
		more=len(sl)-idx
		acc=0
	prev=h