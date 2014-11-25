#_*_ coding: utf-8 _*_

from binary_tree import *

""" [广度优先遍历]
问题： 如何广度优先，遍历一棵两叉树（树的结构定义，见 binary_tree.py）
思路: 利用队列(FIFO)
步骤：
1. 初始：将输入节点放入队列
2. 从队列中get当前节点，访问当前节点后，将当前节点的左、右孩子入队列
3. 重复2，直到队列为空
"""
def BreadthFirst(treeNode):
    '''广度优先遍历二叉树
    [Parameters]
        treeNode <binary_tree.BinTreeNode>: 待遍历树的根节点
    [Return]
        <None>
    '''
    que = NodeQueue()
    que.put(treeNode)
    while (que):
        curNode = que.get()
        visit(curNode)
        if curNode.left:
            que.put(curNode.left)
        if curNode.right:
            que.put(curNode.right)
            
 
 
""" [深度优先遍历：先序]
问题： 如何用非递归的方法，先序遍历二叉树
思路: 利用栈，压入父节点已经被访问的右孩子，并向左追溯，在当前节点为空时，说明栈顶节点的父节点和左兄弟都已经被访问
步骤：
1. 初始：当前节点指向根节点
2. 如果当前节点不为空，访问当前节点，将当前节点的右孩子(如果不为空)入栈，当前节点的左孩子(如果不为空)做新的当前节点
3. 如果当前节点为空，从栈中pop出新的当前节点
4. 重复2、3直到当前节点和栈都为空
"""
def PreOrder(treeNode):
    '''先序遍历二叉树
    [Parameters]
        treeNode <binary_tree.BinTreeNode>: 待遍历树的根节点
    [Return]
        <None>
    '''
    stack = NodeStack()
    curNode = treeNode
    while (curNode or stack):
        if curNode:
            visit(curNode)
            stack.push(curNode.right)
            curNode = curNode.left
        else:
            curNode = stack.pop()
 


""" [深度优先遍历：中序]
问题： 如何用非递归的方法，中序遍历二叉树
思路: 利用栈，压入被追溯了左孩子的当前节点，在当前节点为空时，说明栈顶节点的左孩子已经被访问；访问栈顶节点后，其右孩子成为新的当前节点
步骤：
1. 初始：当前节点指向根节点
2. 如果当前节点不为空，将当前节点入栈，当前节点的左孩子(如果不为空)做新的当前节点
3. 如果当前节点为空，从栈中pop出待访问节点，访问该节点，该节点的右孩子(如果不为空)做新的当前节点
4. 重复2、3直到当前节点和栈都为空
""" 
def InOrder(treeNode):
    '''中序遍历二叉树
    [Parameters]
        treeNode <binary_tree.BinTreeNode>: 待遍历树的根节点
    [Return]
        <None>
    '''
    stack = NodeStack()
    curNode = treeNode
    while (curNode or stack):
        if curNode:
            stack.push(curNode)
            curNode = curNode.left
        else:
            visitingNode = stack.pop()
            visit(visitingNode)
            curNode = visitingNode.right
            



""" [深度优先遍历：后序]
问题： 如何用非递归的方法，后序遍历二叉树
思路: 使用两个栈，A栈记录左孩子已经被追溯过的节点，B栈记录孩子已经被追溯过的结点
1. 初始：当前节点指向根节点
2. 如果当前节点不为空，将当前节点入A栈，当前节点的左孩子(如果不为空)做新的当前节点（追溯左孩子）
3. 如果当前节点为空，说明A栈栈顶节点的左孩子已经被访问；
    3.1 A栈栈顶和B栈栈顶不同（说明A栈栈顶节点的右孩子尚未被访问），将A栈栈顶节点复制一份压入B栈，并追溯A栈栈顶节点的右孩子
    3.2 A栈栈顶和B栈栈顶相同，说明A栈栈顶节点的左、右孩子都被访问了，pop A、B栈节点，访问该节点
4. 重复2、3直到当前节点和栈A都为空
"""            
def PostOrder(treeNode):
    '''后序遍历二叉树
    [Parameters]
        treeNode <binary_tree.BinTreeNode>: 待遍历树的根节点
    [Return]
        <None>
    '''
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
    #===================================
    #  测试用的二叉树
    #===================================
    #             0   
    #          /     \
    #         1       2
    #        / \     / \
    #       3   4   5   6
    #          / \       \
    #         7   8       9
    #        /
    #       10
    #         \
    #         11
    # 
    #====================================
    BreadthFirst(tree[0])
    print ''
    PreOrder(tree[0])
    print ''
    InOrder(tree[0])
    print ''
    PostOrder(tree[0])