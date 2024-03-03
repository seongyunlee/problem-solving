N = int(input())
A = [1,3]
for i in range(2,N):
    A.append((A[i-1]+A[i-2]*2)%10007)
print(A[N-1])