class Solution:
    def isPrime(self, root: int) -> bool:
        if root < 2:
            return False
        for i in range(2, int(root ** 0.5) + 1):
            if root % i == 0:
                return False
        return True

    def isThree(self, n: int) -> bool:
        root = int(n ** 0.5)            # floor
        if root * root != n:
            return False
        return self.isPrime(root)
