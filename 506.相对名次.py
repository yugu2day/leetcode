#
# @lc app=leetcode.cn id=506 lang=python
#
# [506] 相对名次
#

# @lc code=start
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_nums = sorted(nums, reverse=True)
        dic = {}
        for index, num in enumerate(sorted_nums):
            dic[num] = index + 1
        
        res = []
        for num in nums:
            if dic[num] == 1:
                res.append("Gold Medal")
            elif dic[num] == 2:
                res.append("Silver Medal")
            elif dic[num] == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(dic[num]))
        return res

        
# @lc code=end

