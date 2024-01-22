import sys
L = open(0).readlines()
print(*[sum(list(map(int,x.split()))) for x in L],sep="\n")