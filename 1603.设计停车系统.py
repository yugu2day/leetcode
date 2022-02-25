#
# @lc app=leetcode.cn id=1603 lang=python
#
# [1603] 设计停车系统
#

# @lc code=start
class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.d = {
            1:big,
            2:medium,
            3:small
        }


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.d[carType] == 0:
            return False
        self.d[carType] -= 1
        return True



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end

