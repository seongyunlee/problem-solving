from random import randint
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.down = None
class SkipList:
    def __init__(self, list):
        self.head = Node(-1)
        now = self.head
        for n in list:
            now.next = Node(n)
            now.next.prev = now
            now = now.next
        self.build()
    def build(self):
        while True:
            cnt = 0
            now = self.head
            self.head = Node(-1)
            self.head.down = now
            downNow = now
            now = self.head
            while downNow.next:
                if randint(0,1):
                    cnt += 1
                    newNode = Node(downNow.next.val)
                    newNode.prev = now
                    newNode.down = downNow.next
                    now.next = newNode
                    now = now.next
                downNow = downNow.next
            if cnt <= 1:
                break
    def searchAndPop(self, n):
        # search smallest k that k >= n
        now = self.head
        ans = None
        while now:
            if now.next and now.next.val > n and (not ans or ans.val > now.next.val):
                ans = now.next
            if now.next and now.next.val <= n:
                now = now.next
            else:
                if now.down:
                    now = now.down
                else:
                    return self.pop(ans)
    def pop(self, node):
        val = node.val
        now = node
        while now and now.val != -1:
            now.prev.next = now.next
            if now.next: now.next.prev = now.prev
            now = now.down
        return val
    def __str__(self):
        # print all skip list in one depth in line
        depth = self.head
        ret = []
        while depth:
            now = depth
            line = []
            while now.next:
                line.append(str(now.next.val)+"("+str(now.next.prev.val or "None")+")")
                now = now.next
                if now.next:
                    line.append('->')
            depth = depth.down
            ret.append(''.join(line))
        return '\n'.join(ret)
N,M,K = map(int, input().split())
pick = list(map(int, input().split()))
hand = list(map(int, input().split()))
pick.sort()
sl = SkipList(pick)
ans = []
for h in hand:
    ans.append(sl.searchAndPop(h))
print(*ans, sep='\n')

    


        

    