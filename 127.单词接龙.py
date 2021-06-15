#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def diff(word1, word2):
            cnt = 0
            for i in range(0, len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
                if cnt > 1:
                    return cnt
            return cnt

        queue = [beginWord]
        wordList = {str(_) for _ in wordList}
        
        wordList.discard(beginWord)
        if endWord not in wordList:
            return 0

        res = 1

        while queue:
            next_layer = set()
            while queue:
                word = queue.pop(0)
                for w in wordList:
                    if diff(word, w) == 1:
                        next_layer.add(w)
                        if w == endWord:
                            return res + 1
            if next_layer:
                res += 1
                queue = list(next_layer)

                wordList -= next_layer
            else:
                return 0
# @lc code=end

