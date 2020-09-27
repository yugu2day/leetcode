#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        # 获取表节点跑完之后相交的节点
        flag_a, flag_b = False, False
        a, b = headA, headB

        while True:
            if a == b:
                return a
            if not a:
                if flag_a and flag_b:
                    break
                a = headB
                flag_a = True
            else:
                a = a.next

            if not b:
                if flag_a and flag_b:
                    break
                b = headA
                flag_b = True
            else:
                b = b.next
        return None
            
                

        
# @lc code=end

