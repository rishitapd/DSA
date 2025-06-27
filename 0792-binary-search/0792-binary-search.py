class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        n=len(nums)
        
        for i in range(len(nums)):
            mid=(i+n)/2
            
            if nums[mid]==target:
                return mid
            elif nums[i]==target:
                return i    
            elif target>nums[mid]:
                i=mid+1
            else:
                n=mid-1
        return -1           
        