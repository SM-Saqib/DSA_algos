class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums.__len__() > 0 and nums.__len__() <1001 and min(nums) > -1000000 and max(nums) < 1000000:
            return [int(sum(nums[:i])) for i in range(1,nums.__len__()+1)]
        
        
        
