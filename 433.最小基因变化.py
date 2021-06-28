#
# @lc app=leetcode.cn id=433 lang=python
#
# [433] 最小基因变化
#

# @lc code=start
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        self.end = end
        self.res = float('inf')
        self.helper(start, bank, {start}, 0)
        return self.res if self.res != float('inf') else -1


    def helper(self, mid, bank, visited, cur):
        if mid == self.end:
            self.res = min(self.res, cur)
            return 

        for ne in bank:
            # 如果查过则忽略
            # 如果差异为1， 进行继续查找
            if self.diff(mid, ne) == 1 and ne not in visited:
                new_visited = {_ for _ in visited}
                new_visited.add(ne)
                self.helper(ne, bank, new_visited, cur + 1)
    
    def diff(self, n1, n2):
        cnt = 0
        for i in range(0, len(n1)):
            if n1[i] != n2[i]:
                cnt += 1
            if cnt > 1:
                return cnt
        return cnt
            

# @lc code=end

