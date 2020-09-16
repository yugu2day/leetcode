#
# @lc app=leetcode.cn id=743 lang=python
#
# [743] 网络延迟时间
#

# @lc code=start
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        import collections
        dic = collections.defaultdict(list)
        for [u, v, w] in times:
            dic[u].append([v,w])
        
        cache = {i:float("inf") for i in range(1, N+1)}


        def helper(u, t):
            if t >= cache[u]:
                return
            cache[u] = t
            for [v, tmp_t] in dic[u]:
                helper(v, t + tmp_t)
        
        helper(K, 0)
        res = max(cache.values())
        return res if res < float('inf') else -1




# @lc code=end

