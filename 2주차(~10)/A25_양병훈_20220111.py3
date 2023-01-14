import math

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        1. while --> n보다 작거나 같은 경우
        2. 같은면 --> true
        """
        temp = 1
        while temp < n:
            temp = temp*4
        if n ==temp:
            return True
        else:
            return False