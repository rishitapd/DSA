class Solution:
    def getSecondLargest(self, arr):
        if len(arr)<2:
            return -1
        else:
            first=second=int("-1")
            for num in arr:
                if num>first:
                    second=first
                    first=num
                elif num>second and num!=first:
                    second=num
        
        if second=="-1":
            return -1
        else:
            return (second)    
    