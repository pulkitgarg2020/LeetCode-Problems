class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # combine two lists
        newList = nums1 + nums2
        
        # sort two lists
        sortedList = sorted(newList)
        
        if (len(sortedList) == 1):
            return sortedList[0]
        
        index = len(sortedList) % 2
        
        retIndex = int(len(sortedList) / 2)
        
        if index != 0:
            return sortedList[retIndex]
        else:
            return (sortedList[retIndex - 1] + sortedList[retIndex])/2
        
        
