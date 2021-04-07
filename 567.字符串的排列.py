#
# @lc app=leetcode.cn id=567 lang=python
#
# [567] 字符串的排列
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        origin = collections.defaultdict(int)
        for ch in s1:
            origin[ch] += 1

        left, right = 0, len(s1)
        dic = collections.defaultdict(int)
        for _ in s2[left:right]:
            dic[_] += 1

        while right <= len(s2):
            for k, v in origin.items():
                if v != dic.get(k,0):
                    break
            else:
                return True
            
            if right < len(s2):
                dic[s2[left]] -= 1
                dic[s2[right]] += 1
            left += 1
            right += 1
        return False

# @lc code=end

