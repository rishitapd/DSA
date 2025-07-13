class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        start=0
        balance=0
        for i in range(len(s)):
            if s[i]=='(':
                balance+=1
            else:
                balance-=1
            if balance==0:
                result.append(s[start+1:i]) #norally the starting and ending is written as s[start:i+1] so we are removing onw from start and one from end 
                start=i+1
        return ''.join(result)                
        