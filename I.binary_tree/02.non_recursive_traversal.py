#_*_ coding: utf-8 _*_

from binary_tree import *


def BreadthFirst(treeNode):
    que = NodeQueue()
    que.put(treeNode)
    while (que):
        t = que.get()
        visit(t)
        if t.left:
            que.put(t.left)
        if t.right:
            que.put(t.right)
            
 
def PreOrder(treeNode):
    stack = NodeStack()
    curNode = treeNode
    while (curNode or stack):
        if curNode:
            visit(curNode)
            stack.push(curNode.right)
            curNode = curNode.left
        else:
            curNode = stack.pop()
 
 
def InOrder(treeNode):
    stack = NodeStack()
    curNode = treeNode
    while (curNode or stack):
        if curNode:
            stack.push(curNode)
            curNode = curNode.left
        else:
            curNode = stack.pop()
            visit(curNode)
            curNode = curNode.right
            
            
def PostOrder(treeNode):
    leftStack = NodeStack() #当前结点为空时，leftStack标记当前被追溯左孩子的节点
    rightStack = NodeStack() #当前结点为空时，rightStack标记当前被追溯右孩子的节点
    curNode = treeNode
    while curNode or leftStack:
        if curNode:
            leftStack.push(curNode)
            curNode = curNode.left
        elif rightStack and leftStack.top() == rightStack.top():
            leftStack.pop()
            visit(rightStack.pop())
        else:
            rightStack.push(leftStack.top())
            curNode = leftStack.top().right
   
       
            
if __name__ == "__main__":
    tree = MakeSampleBinTree()
    BreadthFirst(tree[0])
    print ''
    PreOrder(tree[0])
    print ''
    InOrder(tree[0])
    print ''
    PostOrder(tree[0])