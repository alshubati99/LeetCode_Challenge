class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # any negative number cannot be a palindrome
        if x <0: 
            return False
        # Variables to hold the original number and reversed number
        original = x
        reversednum = 0

        while x>0:
            digit = x%10            # Extract the last digit
            reversednum = reversednum *10 + digit  # Build the reversed number
            x = x//10     # Remove the last digit
            
        # Compare the reversed number with the original number

        return original == reversednum

solution = Solution()
print(solution.isPalindrome(202))



'''
Space complixty : O(1)
Time Complexity : O(log10(n))

'''