class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        sum =n*(n+1)//2
        total=0
        miss=0
        for i in range(len(nums)):
            total+=nums[i]
        miss=sum-total  
        return miss  

           


        