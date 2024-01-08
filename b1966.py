for _ in range(int(input())):
    n,w=map(int,input().split())
    pr=[[p,x] for x,p in enumerate(list(map(int,input().split())))]
    while True:
        if max([x[0] for x in pr])>pr[0][0]:
            pr=pr[1:]+[pr[0]]
        else:
            if pr[0][1]==w:
                print(n-len(pr)+1)
                break
            pr=pr[1:]