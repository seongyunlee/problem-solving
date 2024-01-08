b=input().split('-')
r=sum(list(map(int,b[b[0]==''].split('+'))))*(-1 if b[0]=='' else 1)
r+=sum([sum(list(map(int,x.split('+'))))*-1 for x in b[(1+(b[0]=='')):]])
print(r)