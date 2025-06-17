class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.strip().split()
        last_word=len(words[-1])
        return last_word


                   
