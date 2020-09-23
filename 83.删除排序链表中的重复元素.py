#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 当前节点设置下一节点为值不相同的节点
        i = head
        while i and i.next:
            while i.next and i.val == i.next.val:
                i.next = i.next.next
            i = i.next
        return head
# @lc code=end

