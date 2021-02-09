#
# @lc app=leetcode.cn id=457 lang=python
#
# [457] 环形数组循环
#

# @lc code=start
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.visited = set()
        for idx, num in enumerate(nums):
            if idx not in self.visited and self.IsCircle(idx, nums, [(num, idx)]):
                return True
        return False
    
    def IsCircle(self, idx, nums, path):
        # path [0] num [1] idx

        if len(path) > 1 and path[-1][1] == path[0][1]:
            return True
        if len(path) > len(nums) + 1:
            return True

        next_idx = (idx + nums[idx]) % len(nums)
        if idx == next_idx or nums[idx] * nums[next_idx] < 0:
            for _, i in path:
                self.visited.add(i)
            return False

        return self.IsCircle(next_idx, nums, path + [(nums[next_idx], next_idx)])
# @lc code=end

