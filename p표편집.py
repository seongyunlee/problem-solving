class Node:
    def __init__(self,idx):
        self.N=idx
        self.next=None
        self.prev=None
        self.present=True
    def recover_self(self):
        if self.prev:self.prev.next=self
        if self.next:self.next.prev=self
        self.present=True
    def delete_self(self):
        self.present=False
        if self.prev:
            self.prev.next=self.next
        if self.next:
            self.next.prev=self.prev
        return self.next if self.next else self.prev
def solution(n, k, cmd):
    global p,now
    erase=[]
    p=[True]*n
    nodes=[Node(i) for i in range(n)]
    for i in range(n):
        if i>0:nodes[i].prev=nodes[i-1]
        if i<n-1:nodes[i].next=nodes[i+1]
    now=nodes[k]
    for c in cmd:
        if c=="Z":
            erase.pop().recover_self()
        elif c=='C':
            erase.append(now)
            now=now.delete_self()
        else:
            t,N=c.split()
            for i in range(int(N)):
                print(now.N)
                if t=='U':now=now.prev
                else:now=now.next
    return ''.join(['O' if k.present else 'X' for k in nodes])
print(solution(8	,2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))