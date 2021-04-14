#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 计算长度，如果长度不满足要求直接返回
        if self.get_len(head) < k:
            return head

        # 先翻转k个节点，然后指向第k+1个节点
        node, next_node = self.reverse(head, k)
        head.next = self.reverseKGroup(next_node, k)

        return node

    def get_len(self, node):
        if not node:
            return 0
        return 1 + self.get_len(node.next)

    def reverse(self, head, k):
        if not head or k == 1:
            return head, head.next
        node = self.reverse(head.next, k-1)
        head.next.next = head
        head.next = None
        return node
# @lc code=end

