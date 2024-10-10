/*
 * @lc app=leetcode.cn id=1936 lang=golang
 *
 * [1936] 新增的最少台阶数
 */

// @lc code=start
func addRungs(rungs []int, dist int) int {
	cur := 0
	res := 0
	for len(rungs) > 0 {
		if cur+dist >= rungs[0] {
			// 可以踏上台阶
			cur = rungs[0]
			rungs = rungs[1:]
		} else {
			// 不能踏上台阶的时候， 需要增加台阶
			gap := rungs[0] - cur
			add := gap / dist
			if gap%dist == 0 {
				add--
			}
			res += add
			cur = rungs[0]
			rungs = rungs[1:]
		}
	}
	return res
}

// @lc code=end

