#
# @lc app=leetcode.cn id=38 lang=python
#
# [38] 外观数列
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(1, n):
            s = self.read(s)
        return s
    
    def read(self, s):
        # describe the s
        l = []
        tmp = ""
        for ch in s:
            if not tmp or ch == tmp[-1]:
                tmp += ch
            else:
                l.append(tmp)
                tmp = ch
        l.append(tmp)
        return ''.join( str(len(ch)) + ch[0]  for ch in l)
# @lc code=end

