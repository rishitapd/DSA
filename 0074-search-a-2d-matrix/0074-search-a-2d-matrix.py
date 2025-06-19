class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix[0])
        n=len(matrix)
        low=0
        high=m*n-1
        
        while low <= high:
            mid=(low+high)/2
            row=mid/m
            col=mid%m
            if target==matrix[row][col]:
                return True
            elif target>matrix[row][col]:
                low=mid+1
            else:
                high=mid-1  
        return False              


        