#
# @lc app=leetcode.cn id=445 lang=python
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.getList(list(str(self.getNum(l1) + self.getNum(l2))))

    def getNum(self, n):
        r = 0
        while n:
            r = r * 10 + n.val
            n = n.next
        return r
    
    def getList(self, n):
        res = ListNode(0)
        r = res
        while n:
            res.next = ListNode(int(n[0]))
            res = res.next
            n.pop(0)
        return r.next
# @lc code=end

