#_*_ coding: utf-8 _*_

"""
使用递归方法，进行二叉树的深度遍历
"""

from binary_tree import *

def PreOrder(treeNode):
    '''先序遍历，先访问树根结点，再访问左子树，再访问右子树
    '''
    if treeNode:
        visit(treeNode)
    if treeNode.left:
        PreOrder(treeNode.left)
    if treeNode.right:
        PreOrder(treeNode.right)
        

def InOrder(treeNode):
    '''中序遍历，先访问左子树，再访问树根结点，最后右子树
    '''
    if treeNode:
        if treeNode.left:
            InOrder(treeNode.left)
        visit(treeNode)
        if treeNode.right:
            InOrder(treeNode.right)
        

def PostOrder(treeNode):
    '''后序遍历，先访问左子树，再访问右子树，最后访问树根结点
    '''
    if treeNode:
        if treeNode.left:
            PostOrder(treeNode.left)
        if treeNode.right:
            PostOrder(treeNode.right)
        visit(treeNode)
        
        

if __name__ == '__main__':
    tree = MakeSampleBinTree()
    PreOrder(tree[0])
    print ''
    InOrder(tree[0])
    print ''
    PostOrder(tree[0])
    
