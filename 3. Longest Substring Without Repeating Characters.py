# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.5

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        le = len(self)
        # list ls = self[0]
        s = len(ls)
        for i in range(le-1):
            if(self[i+1] not in ls):
                s=s+1
                ls.append(self[i+1])
        return s

if __name__ == "__main__":
    print(Solution('abcba'))