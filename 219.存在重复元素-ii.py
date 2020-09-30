#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict
        dic = defaultdict(list)
        for index, num in enumerate(nums):
            if dic[num]:
                if index - dic[num][-1] <= k:
                    return True
            dic[num].append(index)
        return False
# @lc code=end

