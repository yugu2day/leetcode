#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        dic_p = collections.defaultdict(int)
        for ch in p:
            dic_p[ch] += 1

        res = []
        
        dic_s = collections.defaultdict(int)
        for _ in range(0, len(p)):
            dic_s[s[_]] += 1

        for i in range(0, len(s)-len(p)+1):
            for k, v in dic_s.items():
                if dic_s[k] != dic_p[k]:
                    break
            else:
                res.append(i)

            if i +len(p) < len(s):
                dic_s[s[i]] -= 1
                dic_s[s[i+len(p)]] += 1
        return res
# @lc code=end

