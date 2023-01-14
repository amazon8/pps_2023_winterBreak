\class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=num**0.5
        x=x//1
        return (x==num**0.5)