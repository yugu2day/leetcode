#
# @lc app=leetcode.cn id=1171 lang=python
#
# [1171] 从链表中删去总和值为零的连续节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = 0
        arr = []
        l = []

        while head:
            if tmp + head.val == 0:
                return self.removeZeroSumSublists(head.next)
            l.append(head.val)
            arr.append(tmp + head.val)
            tmp = arr[-1]
            head = head.next
        
        res = self.remove(arr, l)

        node = ListNode(0)
        result = node
        for i in range(0, len(res)):
            node.next = ListNode(res[i])
            node = node.next
        return result.next
    
    def remove(self, arr, l):
        # 清除前缀和数组中合为0的部分, 返回原始数组

        for i in range(1, len(arr)):
            for j in range(0, i):
                if arr[i] == arr[j]:
                    # j+1 到 i 的元素和为0
                    l = l[:j+1] + l[i+1:]
                    new_arr = arr[:j+1] + arr[i+1:]
                    new_l = l[:]
                    return self.remove(new_arr, new_l)
        return l
# @lc code=end

