#
# @lc app=leetcode.cn id=526 lang=python
#
# [526] 优美的排列
#

# @lc code=start
class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        def helper(pos, visited):

            if pos == n:
                self.res += 1
            for i in range(1, n+1):

                if i in visited:
                    continue
                if i % (pos+1) == 0 or (pos+1) % i == 0:
                    new_visited = {_ for _ in visited}
                    new_visited.add(i)
                    helper(pos+1, new_visited)
        
        helper(0, set())
        return self.res

# @lc code=end

