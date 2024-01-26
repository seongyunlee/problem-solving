def print_lcs(i, j):
    if s[i][j] == 0:
        return
    if a[i - 1] == b[j - 1]:
        print_lcs(i - 1, j - 1)
        print(a[i - 1], end='')
    else:
        if s[i - 1][j] > s[i][j - 1]:
            print_lcs(i - 1, j)
        else:
            print_lcs(i, j - 1)

N = 1000  # assuming N is defined as 1000 in C++ code
s = [[0] * N for _ in range(N)]
a = input()
b = input()

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            s[i + 1][j + 1] = s[i][j] + 1
        else:
            s[i + 1][j + 1] = max(s[i][j + 1], s[i + 1][j])

print(s[len(a)][len(b)])
print_lcs(len(a), len(b))
