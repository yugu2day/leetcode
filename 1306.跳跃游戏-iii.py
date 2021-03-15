#
# @lc app=leetcode.cn id=1306 lang=python
#
# [1306] 跳跃游戏 III
#

# @lc code=start
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        queue = [start]
        s = set()
        while queue:
            node = queue.pop(0)
            if node not in s:
                s.add(node)
            if arr[node] == 0:
                return True
            if node - arr[node] >= 0 and (node - arr[node]) not in s:
                queue.append(node - arr[node] )
            if node + arr[node] < len(arr) and (node + arr[node]) not in s:
                queue.append(node + arr[node])
        return False
                
# @lc code=end

