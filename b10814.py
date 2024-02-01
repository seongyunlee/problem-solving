import sys
input = sys.stdin.readline
print("\n".join([x for x in sorted([input().rstrip() for i in range(int(input()))],key=lambda x:[int(x.split()[0])])]))