#_*_ coding: utf-8 _*_

import sys
sys.path.append('..')
import common_debug    


""" 字符串的全排列
题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，则输出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。
思路：递归，从未被选择的集合里选一个，放在指定的位置上
"""
def PermutationCore(s, l, pos):
    if not s:
        print ''.join(l)
        return
    for i, a in enumerate(s):
        l[pos] = a
        PermutationCore(s[0:i] + s[i+1:], l, pos+1)
    
def StrPermutation(s):
    PermutationCore(s, [None]*len(s), 0)




""" 字符串的组合
题目：输入一个字符串，打印出该字符串中字符的所有组合。例如输入字符串abc，则输出由字符a、b、c全部或者部分组合a/b/c/ab/ac/abc。
思路：递归，和排列非常类似，主要区别是：
1. 输出字符长度不固定
2. 不能重复计算相同元素的组合，为了不重复，取字符时，要保证取出来的组合是输入字符的子序列
3. 剩余元素不能恰好填满输出数组
"""
def CombinationCore(s, l, pos):
    if len(s) < len(l)-pos: #区别3
        return
    if pos >= len(l): 
        print ''.join(l)
        return
    for i,a in enumerate(s):
        l[pos] = a
        CombinationCore(s[i+1:], l, pos+1) #区别2


def StrCombination(s):
    for n in xrange(1, 1 + len(s)): #区别1
        l = [None] * n
        CombinationCore(s, l, 0)

#test
if __name__ == "__main__":
    print "Permutation:"
    StrPermutation("abcd")
    print "\n\nCombination:"
    StrCombination("bdac")