class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        시작: 11:38
        1. while --> len()>=2 반복
        """

        if len(str(num)) < 2:
            return num
        else:
            while(True):
                sum = 0
                temp = list(map(int, str(num)))
                for i in range(len(temp)):
                    sum += temp[i]
                num = sum
                if len(str(num)) < 2:
                    break
            return num