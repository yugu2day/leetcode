#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 字典存储不同数组长度时的种数，递归得到输入长度为n的数组时的结果

        
        dic = {0:1, 1:1}

        def helper(arr):
            res = 0
            if len(arr) in dic:
                return dic[len(arr)]
            for index in range(0, len(arr)):
                left = helper(arr[:index])
                right = helper(arr[index+1:])
                res += left * right
            dic[len(arr)] = res
            return res

        return helper([_ for _ in range(n)])
# @lc code=end

