import heapq,sys
q=[]
for i in range(int(input())):
    n=int(sys.stdin.readline())
    if n==0:
        print(0 if not q else -heapq.heappop(q))
    else:
        heapq.heappush(q,-n)
