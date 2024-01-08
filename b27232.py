
class TreeNode:
  def __init__(self, key, val):
    self.key = key
    self._leftChild = None
    self._rightChild = None
    self.parent = None

  @property
  def leftChild(self):
    return self._leftChild

  @leftChild.setter
  def leftChild(self, node):
    if self._leftChild:
      self._leftChild.parent = None
    if node:
      node.parent = self
    self._leftChild = node

  @property
  def rightChild(self):
    return self._rightChild

  @rightChild.setter
  def rightChild(self, node):
    if self._rightChild:
      self._rightChild.parent = None
    if node:
      node.parent = self
    self._rightChild = node

  def isRoot(self):
    return not self.parent

  def isLeaf(self):
    return not (self.rightChild or self.leftChild)

  def hasLeftChild(self):
    return self.leftChild is not None

  def hasRightChild(self):
    return self.rightChild is not None

  def isLeftChild(self):
    return self.parent and self.parent.leftChild is self

  def isRightChild(self):
    return self.parent and self.parent.rightChild is self

  def hasAnyChildren(self):
    return not self.isLeaf()

  def hasBothChildren(self):
    return self.hasLeftChild() and self.hasRightChild()

  def findSuccessor(self):
    succ = None
    if self.hasRightChild():
      succ = self.rightChild
      while succ.hasLeftChild():
        succ = succ.leftChild
    return succ

  def sliceOut(self):
    '''트리 내에서 현재 노드를 잘라낸다.
    단, 이 동작은 successor가 되는 노드에만
    한정되는 것으로 간주한다.
    따라서, 현재노드는 왼쪽 자식이 없어야 한다'''
    child = self.rightChild if self.hasRightChild() else None
    self.rightChild = None
    if self.isLeftChild():
      self.parent.leftChild = child
    elif self.isRightChild():
      self.parent.rightChild = child
    # !!! the successor node never has a left child.
class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.length = 0

  def put(self, key, val):
    if self.root is not None:
      self.__put(key, val, self.root)
    else:
      self.root = TreeNode(key, val)
    self.length += 1

  def __put(self, key, val, currentNode):
    targetNode = currentNode
    while True:
      if key < targetNode.key:
        if not targetNode.hasLeftChild():
          targetNode.leftChild = TreeNode(key, val)
          break
        else:
          targetNode = targetNode.leftChild
      else:
        if not targetNode.hasRightChild():
          targetNode.rightChild = TreeNode(key, val)
          break
        else:
          targetNode = targetNode.rightChild
    self.length += 1

  def get(self, key):
    if self.root:
      res = self.__get(key, self.root)
      if res:
        return res.value
    return None

  def __get(self, key, currentNode):
    targetNode = currentNode
    while True:
      if targetNode.key == key:
          return targetNode
      elif key < currentNode.key:
        if targetNode.hasLeftChild():
          targetNode = targetNode.leftChild
        else:
          return None
      else:
        if targetNode.hasRightChild():
          targetNode = targetNode.rightChild
        else:
          return None

  def delete(self, key):
    if self.length == 1 and self.root.key == key:
      self.root = None
      self.length = 0
      return
    node_to_delete = self.__get(key, self.root)
    if not node_to_delete:
      raise KeyError('There is no key in the tree.')
    if node_to_delete.isLeaf():
      if node_to_delete.isLeftChild():
        node_to_delete.parent.leftChild = None
      else:
        node_to_delete.parent.rightChild = None
    elif node_to_delete.hasBothChildren():
      succ = node_to_delete.findSuccessor()
      succ.sliceOut()
      node_to_delete.key, node_to_delete.value = succ.key, succ.value
    else:
      child = node_to_delete.leftChild \
              if node_to_delete.hasLeftChild() else\
              node_to_delete.rightChild
      node_to_delete.leftChild = None
      node_to_delete.rightChild = None
      if node_to_delete.isRoot():
        self.root = child
      elif node_to_delete.isLeftChild():
        node_to_delete.parent.leftChild = child
      else:
        node_to_delete.parent.rightChild = child
    self.length -= 1
N,K=map(int,input().split())
A=list(map(int,input().split()))
nodes=[Node((A[i],i)) for i in range(N)]
P=sorted([(A[i],i) for i in range(K)],reverse=True)
answer=N*N
for i in range(1,K):
    insert(nodes[P[i-1][1]],nodes[P[i][1]])
    answer+=abs(P[i-1][1]-P[i][1])
for i in range(K,N):
    L=nodes[i-K]
    acc=answer+abs(nodes[i-K].next.value-nodes[i-K].prev.value)-abs(nodes[i-K].value-nodes[i-K].prev.value)-abs(nodes[i-K].value-nodes[i-K].next.value)
    pop(nodes[i-K])
    P.pop(0)
    pos=bisect_left(P,(A[i],i))
    if 0<pos<K-1:acc-=abs(P[pos-1]+P[pos])
    if pos>0: acc+=abs(P[pos-1]-A[i])
    if pos<K-1:acc+=abs(P[pos]-A[i])
print(answer)