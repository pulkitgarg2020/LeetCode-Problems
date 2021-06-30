class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        
        if n < 0:
            n = -n
            x = 1/x
            
        while n != 0:
            if n % 2 == 0:
                x = x * x
                n = n/2
            else:
                res = res * x
                n -= 1
        
        return res