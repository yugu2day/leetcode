#
# @lc app=leetcode.cn id=1157 lang=python
#
# [1157] 子数组中占绝大多数的元素
#

# @lc code=start
class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.idx = collections.defaultdict(list)
        for idx, num in enumerate(arr):
            self.idx[num].append(idx)

        

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        for num in self.idx.keys():
            if len(self.idx[num]) < threshold:
                continue
            low = bisect.bisect_left(self.idx[num], left)
            high = bisect.bisect_right(self.idx[num], right)
            if high - low >= threshold:
                return num
        return -1


        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end

