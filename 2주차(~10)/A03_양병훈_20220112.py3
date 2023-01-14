class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        시작: 9:45
        """

        digits = list(map(str, digits))
        string = "".join(digits)
        num = int(string)
        num = num+1
        return (list(map(int, str(num))))