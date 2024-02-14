import sys
input = sys.stdin.readline
A = [1,1,1,2,2,3,4,5,7,9]
for _ in range(100):
    A.append(A[-1]+A[-5])
print(*[A[int(input())-1] for _ in range(int(input()))],sep='\n')