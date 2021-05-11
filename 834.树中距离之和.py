#
# @lc app=leetcode.cn id=834 lang=python
#
# [834] 树中距离之和
#

# @lc code=start
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = [[] for _ in range(N)]
        for baba, erza in edges:
            tree[baba].append(erza)
            tree[erza].append(baba)
        depth = [0] * N     # 各个节点的深度
        count = [0] * N     # 各节点包括自己的子节点数


        # 获取各个节点的深度和包括自己的子节点数
        def dfsForDepthAndCount(node, root):
            count[node] = 1
            for child in tree[node]:
                if child != root:
                    depth[child] = depth[node] + 1
                    dfsForDepthAndCount(child, node)
                    count[node] += count[child]

        dfsForDepthAndCount(0, -1)

        answer = [0] * N
        answer[0] = sum(depth)

        # 对于第一层的某个节点，该节点包括该节点的子节点少走一步 为 s， N-s个节点多走一步 
        def dfsForAnswer(node, root):
            for child in tree[node]:
                if child != root:
                    answer[child] = answer[node] + (N - count[child]) - count[child]
                    dfsForAnswer(child, node)


        dfsForAnswer(0, -1)
        return answer
        
# @lc code=end

