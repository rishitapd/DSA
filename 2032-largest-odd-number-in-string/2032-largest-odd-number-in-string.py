class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        n=len(num)
        i=n
        start=0
        for i in range(n-1,-1,-1):   #(start,stop,step)
            if int(num[i]) % 2 !=0:
                return num[start:i+1]
                

        return ""        
                   
