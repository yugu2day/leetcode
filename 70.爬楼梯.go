/*
 * @lc app=leetcode.cn id=70 lang=golang
 *
 * [70] 爬楼梯
 */

// @lc code=start
func climbStairs(n int) int {
    if n <= 2{
        return n
    }
    dp := make([]int, 3)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i:=3; i <=n; i++{
        dp = append(dp, dp[i-1] + dp[i-2])
    }
    return dp[n]
}
// @lc code=end

