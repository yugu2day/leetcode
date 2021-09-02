#
# @lc app=leetcode.cn id=491 lang=python
#
# [491] 递增子序列
#

# @lc code=start
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for num in nums:
            tmp = res[:]
            for sub in tmp:
                if num >= sub[-1]:
                    new_sub = sub + [num]
                    if new_sub not in res:
                        res.append(new_sub)
            # 将每个数先加入结果，为了找到对应的递增序列，最后过滤单个数的结果
            res.append([num])
        return [_ for _ in res if len(_) > 1]
# @lc code=end

