# -*-coding:UTF-8 -*-
# Author: Wangwenjun
# CreateDate: 2018-12-11

# 需要自己实现链表，知识树上没有这个，所以程序只能直接在网站上跑
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

tag = 0
result = ListNode(0)
head = result

def listToListNode(l):
    import ListNode
    ListNode ls = new ListNode(0)
    for i in range(len(l)):
        ls.val = l[i]
        ls = ls.next
    return ls

def addTwoNumbers(p, q):
    l1 = listToListNode(p)
    l2 = listToListNode(q)
    # 进位标识，如果相加进位，则为1；否则为0
    sum = l1.val+ l2.val+ tag
    tag = sum//10
    result.next = ListNode(sum % 10 )
    result =result.next
        
    if(l1.next != None and l2.next !=None):
        addTwoNumbers(l1.next,l2.next)
    elif(l1.next !=None):
        addTwoNumbers(l1.next, ListNode(0))
    elif(l2.next !=None):
        addTwoNumbers(ListNode(0),l2.next)
    elif(tag >0):
        result.next = ListNode(0)
        result = result.next
    return head.next


if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    addTwoNumbers(l1,l2)