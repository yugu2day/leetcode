#
# @lc app=leetcode.cn id=306 lang=python
#
# [306] 累加数
#

# @lc code=start
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        self.flag = False

        def helper(num, path):
            # print num, path
            if num == "":
                if len(path) >= 3:
                    self.flag = True
                return

            if num[0] == "0":
                if len(num) == 1 and len(path) >= 2:
                    if path[-1] + path[-2] == 0:
                        self.flag = True

                if num[1:].startswith(str(path[-1])):
                    new_path = path[:] + [0]
                    helper(num[1:], new_path)
                return 

            for i in range(1, len(num)):
                second = int(num[:i])
                if num[i:].startswith(str(path[-1] + second)):
                    new_path = path[:]
                    new_path.append(second)
                    helper(num[i:], new_path)
            
            if len(path) >= 2 and int(num) == path[-1] + path[-2]:
                self.flag = True
        
        if num[0] == "0":
            helper(num[1:], [0])
        else:
            for i in range(1, len(num)):
                
                first = int(num[:i])
                path = [first]
                helper(num[i:], path)
        return self.flag  
# @lc code=end

