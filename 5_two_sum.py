class Solution:
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        def getKey(val, index):
            for key, value in index.items():
                if val == value:
                    return key
        
        # dictionary
        index = {}
        
        # resulting list
        res = []
        
        for i in range(0, len(nums)):
            index[i] = nums[i]
        
        for i in range(0, len(nums)):
            comp = target - nums[i]
            if (comp in index.values() and getKey(comp, index) != i):
                res.append(i)
                res.append(getKey(comp, index))
                return res
    
                