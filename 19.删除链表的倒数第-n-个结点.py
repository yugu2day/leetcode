#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow, fast = ListNode(0), ListNode(0)
        slow.next = head
        fast.next = head
        res = slow

        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return res.next
# @lc code=end

