#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        tmp = 0

        while l1 and l2:
            res.next = ListNode(l1.val + l2.val + tmp)
            if res.next.val >= 10:
                tmp = 1
                res.next.val = res.next.val % 10
            else:
                tmp = 0

            l1 = l1.next
            l2 = l2.next
            res = res.next
        
        while l1:
            res.next = ListNode(l1.val + tmp)
            if res.next.val >= 10:
                tmp = 1
                res.next.val = res.next.val % 10
            else:
                tmp = 0
            l1 = l1.next
            res = res.next

        while l2:
            res.next = ListNode(l2.val + tmp)
            if res.next.val >= 10:
                tmp = 1
                res.next.val = res.next.val % 10
            else:
                tmp = 0
            l2 = l2.next
            res = res.next

        if tmp:
            res.next = ListNode(1)
            res.val = res.val % 10

        return head.next
# @lc code=end

