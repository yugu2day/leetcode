#
# @lc app=leetcode.cn id=1657 lang=python
#
# [1657] 确定两个字符串是否接近
#

# @lc code=start
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        s1, s2 = set(), set()
        #计算每个字符次数所包括的字符数
        r1, r2 = self.count(word1), self.count(word2)
        for freq, cnt in r1.items():
            if len(cnt) != len(r2[freq]):
                return False
            s1 = s1 | cnt
            s2 = s2 | r2[freq]
        return True if s1 == s2 else False
    
    def count(self, word):
        cnt = collections.defaultdict(set)
        d = collections.defaultdict(int)
        for ch in word:
            now = d[ch]
            d[ch] += 1
            cnt[now+1].add(ch)
            if now != 0:
                cnt[now].remove(ch)
        return cnt 
# @lc code=end

