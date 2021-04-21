#
# @lc app=leetcode.cn id=817 lang=python
#
# [817] 链表组件
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """

        res = 0
        s = set(G)

        while head:
            if head.val in s:
                res += 1
                while head and head.val in s:
                    s.remove(head.val)
                    head = head.next
            if head:
                head = head.next
        return res


        
# @lc code=end

