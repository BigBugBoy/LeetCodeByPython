# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2018.12.10

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return False
        for i in range(len(nums)-1):
            j=target-nums[i]
            if j in nums[i+1:]:
                return [i,nums[i+1:].index(j) +i+1]
        return False

