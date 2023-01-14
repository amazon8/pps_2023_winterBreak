class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)
        for n in c.elements():
            if c[n]==1:
                return n