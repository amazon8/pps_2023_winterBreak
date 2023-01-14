class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        1. for --> 연산
        """

        res = []

        for i in range(left, right+1):
            temp = list(map(int, str(i)))
            num = 0
            for j in range(len(temp)):
                if temp[j] ==0:
                    continue
                if i % temp[j] ==0:
                    num += 1
            if num == len(temp):
                res.append(i)

        return res