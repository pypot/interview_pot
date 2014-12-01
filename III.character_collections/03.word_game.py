#coding: utf8

import numpy
from collections import defaultdict

'''
题目： 有一个单词库，，现在给出一个字符串，这个字符串中每个字符最多只能使用一次，也可以不用，
根据这个字符串组合成单词库中最长的单词，如果有多个结果，选最优那个，给出时间复杂度的分析。比如输入“aessdnnsadv”,组成最长的是
advances，描述一下具体的算法或者伪码 
思路： 将单词变成一个向量，用numpy.all(w < s) 可以快速判断给定字符串是否包含全部字符
'''


def MakeBitmap(s):
    s = s.lower()
    bitmap = numpy.zeros(27, dtype='int8')
    for i in s:
        pos = ord(i) - ord('a') + 1
        if pos > 0 and pos < 27:
            bitmap[pos] += 1
    bitmap[0] = sum(bitmap[1:])
    return bitmap


def Hit(sbit, wbit):
    return all(wbit <= sbit)


def ScanDict(dictFile):
    dictList = []
    dictMap = defaultdict(lambda: set())
    for w in dictFile:
        w = w.strip()
        b = MakeBitmap(w)
        dictList.append(b)
        dictMap[tuple(b)].add(w)
    dictList.sort(key=lambda x:x[0], reverse=True)
    return dictList, dictMap



def FindBestWord(s, dl, dm):
    b = MakeBitmap(s)
    for i in dl:
        if Hit(b, i):
            return dm[tuple(i)]
    return None
    
    
if __name__ == "__main__":
    dl, dm = ScanDict(open('worddict.txt'))
    while True:
        s = raw_input("give a string:")
        if s == ':q':
            exit(0)
        print FindBestWord(s, dl, dm)