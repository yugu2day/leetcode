#
# @lc app=leetcode.cn id=881 lang=python
#
# [881] 救生艇
#

# @lc code=start
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if l == r:
                res += 1
                return res
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            res += 1
        return res
# @lc code=end

