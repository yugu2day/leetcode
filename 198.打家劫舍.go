/*
 * @lc app=leetcode.cn id=198 lang=golang
 *
 * [198] 打家劫舍
 */

// @lc code=start
func rob(nums []int) int {
    if len(nums) == 1{
        return nums[0]
    }

    first := make([]int, 0)
    first = append(first, nums[0])
    first = append(first, max(nums[0],nums[1]))

    for i:=2; i <len(nums); i++{
        first = append(first, max(first[len(first)-2]+nums[i], first[len(first)-1]))
            }
    return first[len(first)-1]
}

func max(num1, num2 int)int{
    if num1 > num2{
        return num1
    }
    return num2
}
// @lc code=end

