#_*_ coding: utf-8 _*_
'''
问题1：
一个数组所有元素都有2个，只有1个只有一个，找到这个元素。时间复杂度O(n)， 空间复杂度O(1)
'''
 
def FindUniqOne(a):
    return reduce(lambda x,y: x^y, a)



'''
问题2：
一个数组所有元素都有2个，只有2个只有一个，找到这2个元素
'''

def GetNzBitMask(x):
    if not x:
        return -1
    t = x
    while not (t & 1):
        t = t >> 1
    return x / t
    
def FindUniqTwo(a):
    diff = reduce(lambda x,y: x^y, a)
    mask = GetNzBitMask(diff)
    n1, n2 = 0, 0
    for i in a:
        if i & mask:
            n1 ^= i
        else:
            n2 ^= i
    return n1,n2

    
if __name__ == "__main__":
    a = range(98999999, 99999999, 2) * 2 + [99066120]
    print FindUniqOne(a)
    a = range(98999998, 99999998, 2) * 2 + [99011111, 99200999]
    print FindUniqTwo(a)