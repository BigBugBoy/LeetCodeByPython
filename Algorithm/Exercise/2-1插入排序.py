# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.9


# 插入排序，实现伪代码
def insertion_sort(aArray):
    for j in range(1,len(aArray)):
        key = aArray[j]
        i = j - 1
        while (i >0 or i == 0) and aArray[i] > key:
            aArray[i+1] = aArray [i]
            i = i - 1
        aArray[i +1] = key
    print(aArray)


# 重写函数，使之按非升序（而不是非降序)排序
def insertion_sort_dec(aArray):
    for j in range(1,len(aArray)):
        key = aArray[j]
        i = j - 1
        while (i >0 or i == 0) and aArray[i] < key:
            aArray[i+1] = aArray [i]
            i = i - 1
        aArray[i +1] = key
    print(aArray)


# 两个n位二进制整数相加的问题，两个整数分别存储在两个n元数组A和B中
# 这两个数的和按照二进制形式存储在一个（n+1）元数组C中。
# TODO 没看懂这个跟插入排序有什么关系

if __name__ == "__main__":
    # 测试伪代码
    test_Array = [5,2,4,6,1,3]
    insertion_sort(test_Array)

    # 测试降序
    insertion_sort_dec(test_Array)
