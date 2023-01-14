class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        1. a 개수
        2. l 연속 확인
        """

        res = True
        num = 0
        for i in range(len(s)):
            if s.count("A") >= 2:
                res = False
                return res
            elif s[i] == "L":
                if num ==2:
                    res = False
                    return res
                else:
                    num += 1
            else:
                num = 0
        
        return res