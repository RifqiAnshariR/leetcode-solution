class Solution:
    def climbStairs(self, n: int) -> int:
        # if n < 3:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        if n < 3:
            return n
        
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
        
        return b
