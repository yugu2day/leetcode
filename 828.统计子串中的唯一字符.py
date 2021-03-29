#
# @lc app=leetcode.cn id=828 lang=python
#
# [828] 统计子串中的唯一字符
#

# @lc code=start
class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 字符c 出现的index i, j, k
        # 对j位置来说 [i+1:k] 的子串数为j只出现一次的次数; (j + 1 - i) * (k-j)

        pos = collections.defaultdict(list)

        for idx, c in enumerate(s):
            pos[c].append(idx)
        res = 0
        for char, idxs in pos.items():
            for j in range(0, len(idxs)):
                i = -1 if j == 0 else idxs[j-1]
                k = len(s) if j == len(idxs) - 1 else idxs[j+1]
                res += (idxs[j] - i) * (k - idxs[j])

        return res % 1000000007
# @lc code=end

