# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2018.12.25

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
                return []
        a = [] # 记录每一层的平均值
        queue = [(root,1)]
        while len(queue) != 0:
            b = []
            for i in range(len(queue)):
                n,k = queue.pop(0)
                b.append(n.val)
                if n.left is not None:
                    b.append(n.left.val)
                if k.right is not None :
                    b.append(n.right.val)
            a.append(sum(b)/len(b))
        return a