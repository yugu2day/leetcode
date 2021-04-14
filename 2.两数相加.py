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
        head = ListNode(0)
        res = head
        tmp = 0

        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            res.next = ListNode(n1 + n2 + tmp)
            if res.next.val >= 10:
                tmp = 1
                res.next.val %= 10
            else:
                tmp = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            res = res.next
            
        if tmp == 1:
            res.next = ListNode(1)
        return head.next

# @lc code=end

