class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to match the opening and closing brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty; else use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the current closing bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched properly
        return not stack

# Create an instance of the Solution class
solution = Solution()

# Test cases
print(solution.isValid("()"))      # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))      # Output: False
print(solution.isValid("([])"))    # Output: True
print(solution.isValid("((("))     # Output: False



# Intuition:
# Use a stack to keep track of unmatched opening brackets.
# When encountering a closing bracket, check if it matches the top of the stack.
# If there’s any mismatch or leftover opening brackets, the string is invalid.

# Complexity:
# - Time complexity: O(n), where n is the length of the input string
#   (we iterate through the string once and perform O(1) operations for each character).
# - Space complexity: O(n) in the worst case (stack size can grow to the size of the input string
#   if it consists entirely of opening brackets).


