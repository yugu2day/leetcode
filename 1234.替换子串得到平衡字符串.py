#
# @lc app=leetcode.cn id=1234 lang=python
#
# [1234] 替换子串得到平衡字符串
#

# @lc code=start
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        equal = len(s) // 4
        counter = collections.Counter(s)

        left, right = 0, -1
        res = float('inf')

        while right < len(s):

            if counter["Q"] <= equal and counter["W"] <= equal and counter["E"] <= equal and counter["R"] <= equal:

                res = min(res, right-left+1)
                if res == 0:
                    return 0
                counter[s[left]] += 1
                left += 1
            else:
                if right + 1 < len(s):
                    right += 1
                    counter[s[right]] -= 1
                else:
                    break

        return res
# @lc code=end

