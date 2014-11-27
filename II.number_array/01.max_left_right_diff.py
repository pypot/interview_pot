#_*_ coding: utf-8 _*_

"""
题目：在数组中，数字减去它右边的数字得到一个数对之差。求所有数对之差的最大值。例如在数组{2, 4, 1, 16, 7, 5, 11, 9}中，数对之差的最大值是11，是16减去5的结果。
思路：动态规划
规模参数：
1. 数组前缀长度
记录表：
1. 确定记录表：对以每个元素结尾的子数组，记录子数组的最大的元素，和除最后一个元素外的最大差值
2. 压缩记录表：只需要记录最后一个最大差值和最大元素
初始值：
1. 子数组元素小于2个，返回错误
2. 子数组元素为2个，最大元素为第一个元素，最大差值为最后一个差值
递推式：
1. 如果前一个元素比最大元素大，最大元素则为前一个元素 (max[i] = max(num[i], max[i-1])
2. 如果最大元素减去新增值比最大差大，替换掉最大差值（maxDiff[i] = max(maxDiff[i-1]， max[i] - num[i])
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
    