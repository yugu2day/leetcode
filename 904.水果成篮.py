#
# @lc app=leetcode.cn id=904 lang=python
#
# [904] 水果成篮
#

# @lc code=start
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        dic = collections.defaultdict(int)
        left, right = 0, 0
        res = 0

        while right < len(tree):
            dic[tree[right]] += 1

            while left < right and len(dic.keys()) > 2:
                dic[tree[left]] -= 1
                if dic[tree[left]] == 0:
                    dic.pop(tree[left])
                left += 1
            

            right += 1
            res = max(res, sum(dic.values()))

        return res
# @lc code=end

