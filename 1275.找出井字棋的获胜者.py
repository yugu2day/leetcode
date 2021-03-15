#
# @lc app=leetcode.cn id=1275 lang=python
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """

        matrix = [[" "]* 3 for _ in range(3)]
        for i, [r,c] in enumerate(moves):
            if i % 2 == 0:
                matrix[r][c] = "A"
            else:
                matrix[r][c] = "B"
        # print matrix
        arr = [n for row in matrix for n in row]

        if arr[0] == arr[1] == arr[2] != " ":
            return arr[0]
        if arr[3] == arr[4] == arr[5] != " ":
            return arr[3]
        if arr[6] == arr[7] == arr[8] != " ":
            return arr[6]
        if arr[0] == arr[3] == arr[6] != " ":
            return arr[0]
        if arr[1] == arr[4] == arr[7] != " ":
            return arr[1]
        if arr[2] == arr[5] == arr[8] != " ":
            return arr[2]
        if arr[0] == arr[4] == arr[8] != " ":
            return arr[0]
        if arr[2] == arr[4] == arr[6] != " ":
            return arr[2]

        if arr.count(' ') != 0:
            return "Pending"
        else:
            return "Draw"
        
# @lc code=end

