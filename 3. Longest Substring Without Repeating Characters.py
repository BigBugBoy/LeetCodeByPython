# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.5

class Solution:
    def __init__(self, s):
        # 可以不用显示“构造函数”
        """
        :type s: str
        :rtype: int
        """
        self.result = 0

    def lengthOfTheSubstring(self, s):
        le = len(s)
        if le == 0 :return 0
        ls = []
        ls.append(s[0])
        self.result = len(ls)
        maxLen = 1 # 从1开始，前边已经判断过，排除了空列表情况，列表至少有一个
        # maxLs = []
        for i in range(le-1):
            if(s[i+1] not in ls):
                # 下一个字符不在结果队列ls里边，那么进行相关增加操作
                self.result +=1
                ls.append(s[i+1])
                if maxLen <= self.result:
                    maxLen = self.result
                    # maxLs = ls[:]
            else:
                # 此处有两种情况，最后一个字符与当前字符相同，最后一个字符与当前字符不同
                p = ls.index(s[i+1])
                ls.append(s[i+1])
                del ls[:p+1]
                # maxLs = ls[:]
                self.result = len(ls)
        return maxLen

if __name__ == "__main__":
    testAnswer = Solution('abcba')
    print(testAnswer.lengthOfTheSubstring('pwwkew'))