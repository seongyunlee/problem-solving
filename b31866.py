p = input().split()
e = [["5","0"],["2","5"],["0","2"]]
if p in e: print(">")
elif p[::-1] in e: print("<")
elif p[0] == p[1]: print("=")
elif p[1] not in ("5", "2", "0") and p[0] not in ("5", "2", "0"): print("=")
else: print(">" if p[0] in ("5", "2", "0")  else "<")