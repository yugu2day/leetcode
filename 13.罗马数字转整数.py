#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 顺序遍历，顺序保存特殊值
        dic = [('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90), ('CD', 400), ('CM', 900), ('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
        res = 0
        while s:
            for k, v in dic:
                if s.startswith(k):
                    res += v
                    s = s[len(k):]
                    break
        return res




# @lc code=end

