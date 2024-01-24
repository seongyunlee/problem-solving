s = input()
print(*[s.index(chr(x)) if chr(x) in s else -1 for x in range(97,123)],sep=" ")