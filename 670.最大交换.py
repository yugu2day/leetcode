#
# @lc app=leetcode.cn id=670 lang=python
#
# [670] 最大交换
#

# @lc code=start
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 10:
            return num
        
        # 首位数最大，则不需要移动首位数
        # 首位数不是最大，与最后一个最大数交换位置
        def helper(num_list):
            if not num_list:
                return []
            max_n = max(num_list)
            if max_n == num_list[0]:
                return [max_n] + helper(num_list[1:])
                
            i = 0
            for idx, n in enumerate(num_list):
                if max_n == n:
                    i = idx
            num_list[0], num_list[i] = num_list[i], num_list[0]
            return num_list
        
        return int(''.join(helper(list(str(num)))))
# @lc code=end

