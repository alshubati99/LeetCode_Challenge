class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Iterate through the strings starting from the second one
        for s in strs[1:]:
            # Update the prefix to the longest common prefix with the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix


solution = Solution()
strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs2))  # Output: ""


# Intuition:
# The longest common prefix of a list of strings is the largest substring 
# present at the beginning of every string. By iteratively comparing the prefix 
# with each string, we can reduce the prefix until it matches all strings.

# Approach:
# 1. Start by assuming the first string is the longest common prefix.
# 2. Compare this prefix with each subsequent string.
# 3. Gradually trim the prefix until it matches the beginning of the current string.
# 4. If the prefix becomes empty during the process, return an empty string.

# Algorithm: Iterative reduction of prefix using the `startswith` method.

