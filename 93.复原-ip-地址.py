#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def helper(tmp, s):
            if not s and len(tmp) == 4:
                res.append('.'.join(tmp))
                return
            if not s or len(tmp) > 4:
                return 
            helper(tmp + [s[0]], s[1:])
            if len(s) >= 2 and 10 <= int(s[:2]):
                helper(tmp + [s[:2]], s[2:])
            if len(s) >= 3 and 100 <= int(s[:3]) <= 255:
                helper(tmp + [s[:3]], s[3:])
        helper([], s)
        return res
# @lc code=end

