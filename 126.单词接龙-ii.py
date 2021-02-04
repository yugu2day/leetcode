#
# @lc app=leetcode.cn id=126 lang=python
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        dic = collections.defaultdict(list)
        n = len(beginWord)
        for w in wordList:
            for i in range(n):
                dic[w[:i] + '*' + w[i+1:]].append(w)


        queue = [(beginWord, [beginWord])]
        seen, res = set(), []
        while queue:
            tmp = []
            while queue:
                w, path = queue.pop(0)
                if w == endWord: 
                    res.append(path)

                seen.add(w)
                for i in range(n):
                    for v in dic[w[:i] + '*' + w[i+1:]]:
                        if v not in seen:
                            tmp.append((v, path + [v]))
            if res: 
                return res
            queue = tmp
        return []

# @lc code=end

