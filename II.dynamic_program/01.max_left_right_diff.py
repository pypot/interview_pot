#_*_ coding: utf-8 _*_

"""
题目：在数组中，数字减去它右边的数字得到一个数对之差。求所有数对之差的最大值。例如在数组{2, 4, 1, 16, 7, 5, 11, 9}中，数对之差的最大值是11，是16减去5的结果。
"""

def MaxLeftRightDiff(a):
    if len(a) < 2:
        return None
    maxLeft = max(a[0], a[1])
    maxDiff = a[0] - a[1]
    for i in xrange(2, len(a)):
        if a[i-1] > maxLeft:
            maxLeft = a[i-1]
        curDiff = maxLeft - a[i]
        if curDiff > maxDiff:
            maxDiff = curDiff  
    return maxDiff



if __name__ == "__main__":
    a = [2, 4, 1, 16, 7, 5, 11, 9]
    print MaxLeftRightDiff(a)
    