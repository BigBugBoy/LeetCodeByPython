# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2018.12.12


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tag = 0
        head = ListNode(0)
        curr = head
        sum = 0
        while(l1 != None or l2 !=None):
            x = l1.val if l1 !=None else 0
            y = l2.val if l2 !=None else 0
            sum =x + y + tag
            tag = sum//10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if(l1 !=None):l1 = l1.next
            if(l2 !=None):l2 = l2.next
        if(tag>0):
            curr.next = ListNode(tag)
        return head.next