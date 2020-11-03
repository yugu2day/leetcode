#
# @lc app=leetcode.cn id=941 lang=python
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        if len(A) < 3:
            return False
        
        is_up = True # 山脉上升

        for i in range(0, len(A) - 1):
            if A[i] == A[i+1]:
                return False

            if is_up and A[i] > A[i+1]:
                if i == 0:
                    return False

                is_up = False
                continue
            if not is_up and A[i] < A[i+1]:
                return False
        return True if not is_up else False
# @lc code=end

