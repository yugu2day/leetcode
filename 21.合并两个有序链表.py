#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        tmp = res
        while l1 or l2:
            if not l1:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
                continue
            if not l2:
                tmp.next = l1   
                l1 = l1.next
                tmp = tmp.next
                continue
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
            else:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
        return res.next

            

# @lc code=end

