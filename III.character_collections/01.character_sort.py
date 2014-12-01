#_*_ coding: utf-8 _*_

'''
题目：给一个字符串，有大小写字母，要求写一个函数把小写字母放在前面，大写字母放在后面，尽量使用最小的空间、时间复杂度。
思路：类似快排
'''

def CapCmp(x, y):
    if x.islower() and y.isupper():
        return -1
    elif x.isupper() and y.islower():
        return 1
    else:
        return 0


def PythonSysCapSort(s):
    '''使用python内置排序
    '''
    return ''.join(sorted(s, cmp=CapCmp))



def Swap(l, i, j):
    t = l[i]
    l[i] = l[j]
    l[j] = t

def CapSort(s):
    l = list(s)
    i = 0
    j = len(l) - 1
    while i < j:
        while i < j and l[i].islower():
            i += 1
        while j > i and l[j].isupper():
            j -= 1
        Swap(l, i, j)
    return ''.join(l)
    


if __name__ == "__main__":
    s = "DedAbcgKoPrsTUVxxy"
    print PythonSysCapSort(s)
    print CapSort(s)
