#
# @lc app=leetcode.cn id=907 lang=python
#
# [907] 子数组的最小值之和
#

# @lc code=start
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
    
        arr.append(-1)
        stack,res=[-1],0
        for i in range(len(arr)):
            while arr[i]<arr[stack[-1]]:
                idx=stack.pop()
                res+=arr[idx]*(i-idx)*(idx-stack[-1])
            stack.append(i)
        return res%(10**9+7)

# @lc code=end

