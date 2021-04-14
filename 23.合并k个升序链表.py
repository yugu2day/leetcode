#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        new_lists = []
        for i in range(0, len(lists)):
            l, r = i, len(lists) - 1 - i
            if l > r:
                break
            elif l == r:
                new_lists.append(lists[l])
            else:
                new_lists.append(self.mergeTwoList(lists[l], lists[r]))
        return self.mergeKLists(new_lists)
    

    def mergeTwoList(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            head = ListNode(l1.val)
            head.next = self.mergeTwoList(l1.next, l2)
            return head
        else:
            head = ListNode(l2.val)
            head.next = self.mergeTwoList(l1, l2.next)
            return head
# @lc code=end

