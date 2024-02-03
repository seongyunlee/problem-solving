S = []
for _ in range(int(input())):
    A = int(input())
    if A == 0:
        S.pop()
    else:
        S.append(A)
print(sum(S))