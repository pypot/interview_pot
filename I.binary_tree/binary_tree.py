#_*_ coding: utf-8 _*_

"""
二叉树结构定义
"""
class BinTreeNode(object):
    '''树的结构体
    '''
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        
    def evaluate(self, l, r, v):
        self.left = l
        self.right = r
        self.value = v
        
    def __str__(self):
        return str(self.value)



class NodeStack(object):
    '''用来在放树节点的栈
    '''
    def __init__(self):
        self.data = []
    
    def pop(self):
        return self.data.pop()
    
    def top(self):
        return self.data[-1]
    
    def push(self, e):
        self.data.append(e)
        
    def empty(self):
        return not self.data
    
    def __nonzero__(self):
        return bool(self.data)
        

class NodeQueue(object):
    '''用来在放树节点的队列
    '''
    def __init__(self):
        self.data = []
        
    def get(self):
        return self.data.pop(0)
    
    def put(self, e):
        self.data.append(e)

    def empty(self):
        return not self.data
    
    def __nonzero__(self):
        return bool(self.data)
    
    
def MakeSampleBinTree():
    '''生成一棵测试用的二叉树
                0   
             /     \
            1       2
           / \     / \
          3   4   5   6
             / \       \
            7   8       9
    '''
    tree = [BinTreeNode() for i in range(10)]
    tree[9].evaluate(None, None, 9)
    tree[8].evaluate(None, None, 8)
    tree[7].evaluate(None, None, 7)
    tree[6].evaluate(None, tree[9], 6)
    tree[5].evaluate(None, None, 5)
    tree[4].evaluate(tree[7], tree[8], 4)
    tree[3].evaluate(None, None, 3)
    tree[2].evaluate(tree[5], tree[6], 2)
    tree[1].evaluate(tree[3], tree[4], 1)
    tree[0].evaluate(tree[1], tree[2], 0)
    return tree

import sys
def visit(treeNode):
    sys.stdout.write("%s, " % treeNode)

    
if __name__ == "__main__":
    tree = MakeSampleBinTree()
    print tree[0].left