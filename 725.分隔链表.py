#
# @lc app=leetcode.cn id=725 lang=python
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = self.getLength(root)
        sub = length / k    # 每个分组的基础数
        add = length % k    # 需要sub+1的分组数
        res = []


        for i in range(0, k):
            tmp = ListNode(0)
            node = tmp
            tmp.next = root

            for i in range(0, sub):
                tmp = tmp.next
            if add != 0:
                tmp = tmp.next
                add -= 1
            
            root = tmp.next
            tmp.next = None
            res.append(node.next)
        return res

    def getLength(self, root):
        if not root:
            return 0
        return 1 + self.getLength(root.next)
# @lc code=end

