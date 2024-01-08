from itertools import permutations
input()
card=input().split()
perm=permutations(card,len(card))
follow = {i:[] for i in range(len(card))}
num=9999999999999999
for p in perm:
	st=p[0]
	for n in p[1:]:
		if st[-1]==n[0]:
			st+=n[1]
		else:
			st+=n
	if int(st)<num:
		num=int(st)
print(num)