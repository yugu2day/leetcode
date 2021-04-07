#
# @lc app=leetcode.cn id=763 lang=python
#
# [763] 划分字母区间
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []

        c = collections.Counter(S)
        left, right = 0, 1
        dic = collections.defaultdict(int)
        dic[S[left]] = 1

        while right <= len(S):
            for k, v in dic.items():
                if v < c[k]:
                    break
            else:
                res.append(right-left)
                left = right
                right = left + 1
                if left < len(S):
                    dic = collections.defaultdict(int)
                    dic[S[left]] = 1
                continue
            
            if right < len(S):
                dic[S[right]] += 1
            right += 1
        return res
# @lc code=end

