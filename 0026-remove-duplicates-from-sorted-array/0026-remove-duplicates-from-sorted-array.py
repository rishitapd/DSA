class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        for j in range(len(nums)):
            if i<j and nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                j+=1
                i+=1
            else:
                j+=1    
        return i+1        

        