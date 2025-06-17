class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix=prefix[:-1]
                if prefix=="":
                    return ""
        return prefix        




        