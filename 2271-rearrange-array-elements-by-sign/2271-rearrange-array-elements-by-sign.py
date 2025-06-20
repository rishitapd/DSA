class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=0
        neg=1
        i=0
        arr=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                arr[pos]=nums[i]
                pos+=2
            else:
                arr[neg]=nums[i]
                neg+=2
        return arr       
