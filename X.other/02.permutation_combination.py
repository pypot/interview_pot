#_*_ coding: utf-8 _*_

gOutBuf = []

def Output(a):
    gOutBuf.append(a)
    
def CleanOut():
    global gOutBuf
    gOutBuf = []
    
def ShowOut():
    print '\n'.join(gOutBuf)
    


"""
题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，则输出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。
思路：递归，从未被选择的集合里选一个，放在指定的位置上
"""
def PermutationCore(s, l, pos):
    if not s:
        Output(''.join(l))
        return
    for i, a in enumerate(s):
        l[pos] = a
        PermutationCore(s[0:i] + s[i+1:], l, pos+1)
    
def StrPermutation(s):
    PermutationCore(s, [None]*len(s), 0)



def CombinationCore(s, l, pos):
    if len(s) < len(l)-pos:
        return
    if pos >= len(l) or not s:
        print ''.join(l)
        return
    for i,a in enumerate(s):
        l[pos] = a
        CombinationCore(s[i+1:], l, pos+1)


def StrCombination(s):
    s = sorted(s)
    for n in xrange(1, 1 + len(s)):
        l = [None] * n
        CombinationCore(s, l, 0)

#test
if __name__ == "__main__":
    StrPermutation("abcde")
    print len(gOutBuf)
    #ShowOut()
    CleanOut()
    StrCombination("abcd")
    ShowOut()