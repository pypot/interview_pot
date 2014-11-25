#_*_ coding: utf-8 _*_

from binary_tree import *

""" [求二叉树深度]
问题：求给定二叉树的深度，如何使用递归 、非递归实现？
思路：
A. 递归：当前树（以当前结点为根的树）的深度 = 左子树和右子树较大的深度 + 1
B. 非递归：非常类似后序遍历，记录A栈的最大深度。当左子树和右子树都已经入过栈，则包含栈顶节点的路径的最大深度已经算过；弹出该节点，尝试计算不包含该节点的其它路径深度。
"""
def RecursiveGetDepth(treeNode):
    '''递归获得二叉树尝试
    [Parameters]
        treeNode <binary_tree.BinTreeNode>: 待遍历树的根节点
    [Return]
        <int> 二叉树深度
    '''
    if not treeNode:
        return 0
    return max(RecursiveGetDepth(treeNode.left), RecursiveGetDepth(treeNode.right)) + 1


def NonRecursiveGetDepth(treeNode):
    '''非递归获得二叉树尝试，和后序遍历类似
    [Parameters]
        treeNode <binary_tree.BinTreeNode>: 待遍历树的根节点
    [Return]
        <int> 二叉树深度
    '''
    stackA = NodeStack()
    stackB = NodeStack()
    maxDepth = 0
    curNode = treeNode
    while curNode or stackA:
        if curNode:
            stackA.push(curNode)
            if stackA.depth() > maxDepth:
                maxDepth = stackA.depth()
            curNode = curNode.left
        elif stackB and stackA.top() == stackB.top():
            stackA.pop()
            stackB.pop()
        else:
            tmp = stackA.top()
            stackB.push(tmp)
            curNode = tmp.right
    return maxDepth


GetDepth = NonRecursiveGetDepth  #提供简单的函数名




"""
问题：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。如果某二叉树中任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
思路：
A. 使用GetDepth函数，自顶向下判断每个节点
B. 自顶向下判断每个节点，把RecursiveGetDepth和判断平衡一起做，不重复计算树高
"""

def IsBalanceSimple(treeNode):
    '''判断二叉树平衡的简单实现，存在问题是：有很多子树被重复计算Depth
    [Parameters]
        treeNode <binary_tree.BinTreeNode>: 子树的根节点
    [Return]
        <bool> 子树是否平衡
        <int> 子树的高度
    '''
    if not treeNode:
        return True
    if abs(GetDepth(treeNode.left) - GetDepth(treeNode.right)) > 1:
        return False
    return IsBalanceSimple(treeNode.left) and IsBalanceSimple(treeNode.right)

    

def IsBalanceEfficient(treeNode):
    '''判断二叉树平衡的高效率实现，把RecursiveGetDepth和判断平衡一起做，不会重复计算树高
    [Parameters]
        treeNode <binary_tree.BinTreeNode>: 子树的根节点
    [Return]
        <bool> 子树是否平衡
        <int> 子树的高度
    '''
    if not treeNode:
        return True, 0
    flag, ld = IsBalanceEfficient(treeNode.left)
    if not flag:
        return False, ld + 1  #flag为False， ld + 1无意义
    flag, rd = IsBalanceEfficient(treeNode.right)
    if not flag:
        return False, rd + 1  #flag为False， rd + 1无意义
    return abs(ld - rd) <= 1, max(ld, rd) + 1
    
    


#测试
if __name__ == "__main__":
    tree = MakeSampleBinTree()
    print RecursiveGetDepth(tree[0])
    print RecursiveGetDepth(tree[6])
    print RecursiveGetDepth(tree[7])
    
    print NonRecursiveGetDepth(tree[0])
    print NonRecursiveGetDepth(tree[6])
    print NonRecursiveGetDepth(tree[7])
    
    print IsBalanceSimple(tree[0])
    print IsBalanceSimple(tree[1])
    print IsBalanceSimple(tree[2])
    
    print IsBalanceEfficient(tree[0])
    print IsBalanceEfficient(tree[1])
    print IsBalanceEfficient(tree[2])