#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        if not head.next.next:
            if head.val <= head.next.val:
                return head
            else:
                r = head.next
                head.next.next = head
                head.next = None
                return r
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(mid)

        
        return self.combineLists(l1, l2)
    

    def combineLists(self, l1, l2):
        # 合并有序链表
        res = ListNode(0)
        tmp = res
        while l1 or l2:
            v1 = l1.val if l1 else float('inf')
            v2 = l2.val if l2 else float('inf')

            if v1 <= v2:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        return res.next
# @lc code=end

