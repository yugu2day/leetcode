#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 构建首字符的dict方便检索
        d = collections.defaultdict(list)
        for word in wordDict:
            d[word[0]].append(word)

        cur = 0
        mem = set()
        return self.helper(0, s, d, mem)
    
    def helper(self, cur, s, d, mem):

        if cur == len(s):
            return True

        # 避免被重复计算
        if cur in mem:
            return False
        
        start_ch = s[cur]
        for word in d.get(str(start_ch), []):

            if s[cur:].startswith(word):
                if self.helper(cur+len(word), s, d, mem):
                    return True
        mem.add(cur)
        return False
# @lc code=end

