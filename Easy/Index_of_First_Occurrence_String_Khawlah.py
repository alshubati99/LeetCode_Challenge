class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
    
    # Iterate over possible starting indices
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches needle
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # If no match is found, return -1
        return -1
    


    """

Time Complexity :
In the worst case, we check every possible starting index of haystack (up to n−m+1, where n is the length of haystack and m is the length of needle).
For each starting index, we compare up to m characters.
Thus, the time complexity is O((n−m+1)⋅m), which simplifies to O(n⋅m) in the worst case.
Space Complexity :
We only use a few variables for indexing and slicing, so the space complexity is O(1).
    
    
    """