#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        counter_t = collections.Counter(t)
        counter_dic = collections.defaultdict(int)

        res = ""
        left, right = 0, -1
        while left < len(s) and right < len(s):
            flag = False  # 继续向右移动的标识 
            for k, v in counter_t.items():
                if counter_dic[k] < v:
                    flag = True
                    break
            
            if flag and right + 1 < len(s):
                counter_dic[s[right+1]] += 1
                right += 1

            else:
                if not flag:
                    res = s[left:right+1] if not res or len(res) > (right-left) else res
                    counter_dic[s[left]] -= 1
                    left += 1
                else:
                    break
        return res
# @lc code=end

