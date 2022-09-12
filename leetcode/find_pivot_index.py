class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 == nums.__len__():
            return 0
        if (1 < nums.__len__() <=10000) and min(nums)>= -1000 and max(nums)<= 1000:
            middle_index = int(nums.__len__()//2)
            for i in range(-middle_index,middle_index):
                # print(sum(nums[:middle_index+i]), ":  :",sum(nums[middle_index+i+1:]))
                if(sum(nums[:middle_index+i]) == sum(nums[middle_index+i+1:])):
                    return middle_index+i
        return -1
            # return middle_index
