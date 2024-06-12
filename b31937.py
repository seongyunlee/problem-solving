N,M,K = map(int, input().split())
virus = set(map(int, input().split()))
log = [list(map(int, input().split())) for _ in range(M)]
log.sort(key=lambda x: x[0])
for v in virus:
    die = set([v])
    for _, frm, to in log:
        if frm in die:
            die.add(to)
    if die == virus:
        print(v)
        break