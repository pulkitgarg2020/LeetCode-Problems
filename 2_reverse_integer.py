import math

class Solution:
    def reverse(self, x: int) -> int:
        
        flag = 0
        
        # for a negative number
        if (x < 0):
            flag = 1
            x = x * (-1)
        
        num_len = len(str(x))
        
        # resulting number
        res = 0
        
        multiplier = num_len - 1
        
        # for loop for reversing the number
        for i in range(0, num_len):
            res = res + ((int(x / math.pow(10, i)) % 10) * math.pow(10, multiplier))
            multiplier = multiplier - 1
        
        if flag == 1:
            res = res * (-1)
        
        # checking if the number goes outside the range of 32 bit
        # integer range
        if res < math.pow(-2, 31) or (res > math.pow(2, 31) - 1):
            res = 0
            
        return int(res)
        