#
# @lc app=leetcode.cn id=424 lang=python
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        left, right = 0, 0
        max_count = 0
        dic = collections.defaultdict(int)
        while right < len(s):
            dic[s[right]] += 1
            max_count = max(max_count, dic[s[right]])
            right += 1

            while right - left > max_count + k:
                # 当k个数不够用
                dic[s[left]] -= 1
                left += 1
            
            res = max(res, right-left)
        return res
        
# @lc code=end

