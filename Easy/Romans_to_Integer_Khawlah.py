class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define a dictionary to map Roman numerals to their integer values
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0  # Initialize total to 0
        prev_value = 0  # To track the value of the previous numeral

        # Loop through the Roman numeral string in reverse order
        for char in reversed(s):
            current_value = roman_to_int[char]  # Get the integer value of the current numeral

            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                # Otherwise, add it to the total
                total += current_value

            # Update the previous value for the next iteration
            prev_value = current_value

        return total

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))      # Output: 3
    print(solution.romanToInt("LVIII"))    # Output: 58
    print(solution.romanToInt("MCMXCIV"))  # Output: 1994


    
# Intuition
# The Roman numeral system uses subtraction in specific cases (e.g., IV for 4 and IX for 9).
# By iterating over the string in reverse order, we can efficiently decide when to subtract or add 
# the value of a Roman numeral based on its relation to the next numeral.

# Approach
# 1. Create a mapping of Roman numeral characters to their integer values.
# 2. Iterate through the string in reverse order to process numerals from right to left.
# 3. Use a variable to track the previous numeral's value:
#    - If the current numeral is smaller than the previous one, subtract its value.
#    - Otherwise, add its value.
# 4. Return the accumulated total.

# Complexity
# - Time complexity: O(n), where n is the length of the string.
#   - We process each character in the string exactly once.
# - Space complexity: O(1).
#   - The mapping dictionary and a few scalar variables are used, which do not scale with the input size.

