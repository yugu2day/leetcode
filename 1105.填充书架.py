#
# @lc app=leetcode.cn id=1105 lang=python
#
# [1105] 填充书架
#

# @lc code=start
class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        # dp[i] 表示前i本书的最小高度
        dp = [float('inf')] * (len(books)+1)
        dp[0] = 0
        for i in range(1, len(books)+1):
            
            width, h = 0, 0
            j = i
            while j > 0:
                width += books[j-1][0]
                if width > shelf_width:
                    break
                # 可以和前面的书放在一层
                h = max(books[j-1][1], h)
                dp[i] = min(dp[i], dp[j-1]+h)   
                j -= 1

        return dp[-1]

        
# @lc code=end

