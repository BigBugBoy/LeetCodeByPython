# -*-coding:UTF-8 -*-
# Author: Wangwenjun
# CreateDate: 2018-12-9
# FinishDate: 2018-12-9


def twoSum(nums, target):
    if len(nums)<=1:
        return False
    for i in range(len(nums)-1):
        j=target-nums[i]
        if j in nums[i+1:]:
            return [i,nums[i+1:].index(j) +i+1]
    return False

if __name__ == '__main__':
    print(twoSum([3,2,4],6))
    print(twoSum([3,3],6))


